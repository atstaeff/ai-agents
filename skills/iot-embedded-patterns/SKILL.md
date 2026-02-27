---
name: iot-embedded-patterns
description: IoT, embedded systems, and industrial automation best practices for sensors, actuators, PLCs, and edge computing
---

# IoT & Embedded Patterns Skill

## Instructions for AI

Apply IoT, embedded systems, and industrial automation best practices when designing, implementing, or reviewing systems that involve sensors, actuators, PLCs, communication protocols (MQTT, OPC UA, Modbus), and edge computing. Use this skill for anything related to hardware-software integration, real-time data acquisition, and industrial IoT architectures.

## Core Patterns

### 1. Sensor Abstraction Layer

Decouple business logic from hardware-specific sensor drivers.

```python
from typing import Protocol
from dataclasses import dataclass, field
from datetime import datetime, UTC

class SensorDriver(Protocol):
    """Hardware-agnostic sensor interface."""
    async def read(self) -> float: ...
    @property
    def sensor_id(self) -> str: ...
    @property
    def unit(self) -> str: ...
    @property
    def is_healthy(self) -> bool: ...

@dataclass(frozen=True)
class SensorReading:
    sensor_id: str
    value: float
    unit: str
    timestamp: datetime = field(default_factory=lambda: datetime.now(UTC))
    quality: str = "good"  # good | uncertain | bad | out_of_range

# Concrete implementation for analog input
class AnalogSensor:
    def __init__(self, channel: int, sensor_id: str, unit: str, scale: float = 1.0, offset: float = 0.0) -> None:
        self._channel = channel
        self._sensor_id = sensor_id
        self._unit = unit
        self._scale = scale
        self._offset = offset

    async def read(self) -> float:
        raw = await self._read_adc(self._channel)
        return raw * self._scale + self._offset

    @property
    def sensor_id(self) -> str: return self._sensor_id

    @property
    def unit(self) -> str: return self._unit

    @property
    def is_healthy(self) -> bool: return True

    async def _read_adc(self, channel: int) -> float:
        """Platform-specific ADC read — override per hardware."""
        ...
```

### 2. Actuator Command Pattern

Safe, auditable actuator control with state validation.

```python
from enum import Enum
from dataclasses import dataclass
from typing import Protocol

class ActuatorState(str, Enum):
    IDLE = "idle"
    RUNNING = "running"
    ERROR = "error"
    SAFE_STATE = "safe_state"
    MAINTENANCE = "maintenance"

@dataclass(frozen=True)
class ActuatorCommand:
    actuator_id: str
    action: str        # "start", "stop", "set_speed", "set_position"
    value: float = 0.0
    source: str = "local"  # "local" | "remote" | "auto"

class Actuator(Protocol):
    """Hardware-agnostic actuator interface."""
    def execute(self, command: ActuatorCommand) -> bool: ...
    def safe_state(self) -> None: ...
    @property
    def state(self) -> ActuatorState: ...
    @property
    def actuator_id(self) -> str: ...

class SafeActuatorProxy:
    """Wrapper that enforces safety checks before actuator commands."""

    def __init__(self, actuator: Actuator, interlocks: list["InterlockCheck"]) -> None:
        self._actuator = actuator
        self._interlocks = interlocks

    def execute(self, command: ActuatorCommand) -> bool:
        for check in self._interlocks:
            if not check.is_satisfied():
                self._actuator.safe_state()
                return False
        return self._actuator.execute(command)
```

### 3. MQTT Topic Design

```
# ISA-95 / Sparkplug B inspired hierarchy
{namespace}/{group_id}/{message_type}/{edge_node_id}/{device_id}

# Practical hierarchy
site/{site}/area/{area}/line/{line}/device/{device}/{channel}

# Channels per device:
#   /telemetry    — Sensor data (device → cloud)
#   /command      — Control commands (cloud → device)
#   /status       — Device health/state (device → cloud)
#   /alarm        — Alarm events (device → cloud)
#   /config       — Configuration updates (cloud → device)
#   /ota          — Firmware updates (cloud → device)

# QoS Guidelines:
#   QoS 0 — High-frequency telemetry (> 1 Hz), loss acceptable
#   QoS 1 — Standard telemetry, alarms, status (at-least-once)
#   QoS 2 — Critical commands, config changes (exactly-once)
```

### 4. Edge Data Pipeline

```python
"""Pipeline pattern: Acquire → Validate → Aggregate → Transform → Publish"""
import asyncio
from collections import deque
from dataclasses import dataclass

@dataclass
class PipelineStage:
    """Base for pipeline stages."""
    name: str

class AcquisitionStage(PipelineStage):
    """Read from sensor drivers at defined interval."""
    async def execute(self, sensor: "SensorDriver") -> "SensorReading":
        value = await sensor.read()
        return SensorReading(sensor.sensor_id, value, sensor.unit)

class ValidationStage(PipelineStage):
    """Plausibility checks: range, rate-of-change, stuck-at."""
    def __init__(self, min_val: float, max_val: float, max_roc: float) -> None:
        super().__init__("validation")
        self.min_val = min_val
        self.max_val = max_val
        self.max_roc = max_roc  # max rate of change per second
        self._last: float | None = None

    def execute(self, reading: "SensorReading") -> "SensorReading":
        quality = "good"
        if reading.value < self.min_val or reading.value > self.max_val:
            quality = "out_of_range"
        if self._last is not None and abs(reading.value - self._last) > self.max_roc:
            quality = "spike"
        self._last = reading.value
        return SensorReading(reading.sensor_id, reading.value, reading.unit, quality=quality)

class AggregationStage(PipelineStage):
    """Sliding window statistics."""
    def __init__(self, window_size: int = 60) -> None:
        super().__init__("aggregation")
        self._buffer: deque[float] = deque(maxlen=window_size)

    def execute(self, value: float) -> dict[str, float]:
        self._buffer.append(value)
        values = list(self._buffer)
        return {
            "mean": sum(values) / len(values),
            "min": min(values),
            "max": max(values),
            "count": len(values),
        }
```

### 5. Protocol Gateway Pattern

```python
"""Bridge between industrial protocols and MQTT."""
from typing import Protocol
from dataclasses import dataclass

class IndustrialProtocol(Protocol):
    """Abstraction over PLC communication protocols."""
    def connect(self) -> None: ...
    def disconnect(self) -> None: ...
    def read(self, address: str) -> any: ...
    def write(self, address: str, value: any) -> None: ...

@dataclass
class TagMapping:
    """Maps an industrial tag to an MQTT topic."""
    tag_name: str            # PLC variable name
    source_address: str      # Protocol-specific address
    mqtt_topic: str          # Target MQTT topic
    data_type: str           # "float", "int", "bool"
    poll_interval_ms: int    # Polling interval
    deadband: float = 0.0    # Only publish if change exceeds deadband

class ProtocolGateway:
    """Translates between industrial protocols and MQTT."""

    def __init__(
        self,
        protocol: IndustrialProtocol,
        publisher: "MQTTPublisher",
        mappings: list[TagMapping],
    ) -> None:
        self._protocol = protocol
        self._publisher = publisher
        self._mappings = mappings
        self._last_values: dict[str, any] = {}

    async def poll_cycle(self) -> None:
        for mapping in self._mappings:
            value = self._protocol.read(mapping.source_address)
            last = self._last_values.get(mapping.tag_name)

            # Deadband filtering
            if last is not None and isinstance(value, (int, float)):
                if abs(value - last) < mapping.deadband:
                    continue

            self._last_values[mapping.tag_name] = value
            self._publisher.publish_telemetry(
                TelemetryMessage(
                    device_id=mapping.tag_name,
                    values={mapping.tag_name: value},
                )
            )
```

### 6. Store-and-Forward Pattern

```python
"""Buffer messages when broker is unreachable, replay on reconnect."""
import json
import sqlite3
from pathlib import Path
from dataclasses import dataclass

@dataclass
class BufferedMessage:
    topic: str
    payload: str
    qos: int
    timestamp: float

class StoreAndForward:
    """SQLite-backed message buffer for offline operation."""

    def __init__(self, db_path: str = "/var/lib/iot/buffer.db") -> None:
        self._db = sqlite3.connect(db_path)
        self._db.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic TEXT NOT NULL,
                payload TEXT NOT NULL,
                qos INTEGER DEFAULT 1,
                timestamp REAL NOT NULL,
                sent INTEGER DEFAULT 0
            )
        """)

    def buffer(self, msg: BufferedMessage) -> None:
        self._db.execute(
            "INSERT INTO messages (topic, payload, qos, timestamp) VALUES (?, ?, ?, ?)",
            (msg.topic, msg.payload, msg.qos, msg.timestamp),
        )
        self._db.commit()

    def replay(self, publisher: "MQTTPublisher", batch_size: int = 100) -> int:
        cursor = self._db.execute(
            "SELECT id, topic, payload, qos FROM messages WHERE sent = 0 ORDER BY timestamp LIMIT ?",
            (batch_size,),
        )
        count = 0
        for row in cursor.fetchall():
            msg_id, topic, payload, qos = row
            publisher._client.publish(topic, payload, qos=qos)
            self._db.execute("UPDATE messages SET sent = 1 WHERE id = ?", (msg_id,))
            count += 1
        self._db.commit()
        return count

    def cleanup(self, max_age_hours: int = 72) -> None:
        """Remove old sent messages."""
        import time
        cutoff = time.time() - (max_age_hours * 3600)
        self._db.execute("DELETE FROM messages WHERE sent = 1 AND timestamp < ?", (cutoff,))
        self._db.commit()
```

## Industrial PLC Integration

### Siemens S7 — Tag Mapping

| DB   | Offset | Type  | Description         | MQTT Topic Suffix |
|------|--------|-------|---------------------|-------------------|
| DB10 | 0.0    | REAL  | Temperature Zone 1  | /temp/zone1       |
| DB10 | 4.0    | REAL  | Temperature Zone 2  | /temp/zone2       |
| DB10 | 8.0    | REAL  | Pressure Main       | /pressure/main    |
| DB10 | 12.0   | INT   | Motor Speed RPM     | /motor/speed      |
| DB10 | 14.0   | BOOL  | Motor Running       | /motor/state      |
| DB20 | 0.0    | BOOL  | Emergency Stop      | /safety/estop     |

### Beckhoff TwinCAT — Variable Mapping

| PLC Variable             | Type   | Description          |
|--------------------------|--------|----------------------|
| MAIN.fTemperature        | LREAL  | Process Temperature  |
| MAIN.bMotorRunning       | BOOL   | Motor State          |
| MAIN.nMotorSpeed         | INT    | Motor Speed (RPM)    |
| MAIN.stSensor.fPressure  | REAL   | Pressure Sensor      |
| GVL.bEmergencyStop       | BOOL   | E-Stop Status        |

### Revolution Pi — Module Configuration

| Module      | Position | I/O Type        | Use Case            |
|-------------|----------|-----------------|---------------------|
| RevPi Core  | Base     | CPU + Ethernet  | Edge Gateway        |
| DIO         | Right 1  | 14 DI / 14 DO   | Digital I/O         |
| AIO         | Right 2  | 4 AI / 2 AO     | Analog Sensors      |
| MIO         | Right 3  | Mixed I/O       | Flexible I/O        |
| Gateway     | Right 4  | Modbus/CANopen  | Protocol Bridge     |

## Mechatronics Patterns

### Closed-Loop Control

```
Setpoint → [PID Controller] → [Actuator] → [Process] → [Sensor] ─┐
    ↑                                                              │
    └──────────────────────────────────────────────────────────────┘
                        Feedback Loop
```

### Motion Control State Machine

```
┌──────────┐     enable      ┌──────────┐    start     ┌──────────┐
│  DISABLED │──────────────→ │  STANDBY  │────────────→│  RUNNING  │
│           │←──────────────  │           │←────────────│           │
└──────────┘     disable     └─────┬─────┘    stop     └─────┬─────┘
                                   │                          │
                              error│                     error│
                                   ↓                          ↓
                              ┌──────────┐              ┌──────────┐
                              │  FAULT   │              │  FAULT   │
                              │          │──── reset ──→ │          │
                              └──────────┘              └──────────┘
```

## Communication Protocols Matrix

| Protocol  | Use Case                | Speed      | Determinism | Range       |
|-----------|-------------------------|------------|-------------|-------------|
| MQTT      | Telemetry, Cloud        | Medium     | No          | WAN / LAN   |
| OPC UA    | Industrial Interop      | Medium     | Optional    | LAN         |
| Modbus TCP| Legacy Devices          | Low-Medium | No          | LAN         |
| Modbus RTU| Serial Devices          | Low        | No          | Local       |
| EtherCAT  | Real-Time Motion        | Very High  | Yes (µs)    | LAN         |
| PROFINET  | Siemens Ecosystem       | High       | Yes (ms)    | LAN         |
| CANopen   | Embedded / Automotive   | Medium     | Optional    | Bus (40m)   |
| IO-Link   | Smart Sensors           | Low-Medium | No          | Point (20m) |

## Best Practices

✅ Abstrahere Hardware hinter Interfaces (Protocol pattern)
✅ Verwende Plausibilitaetschecks fuer alle Sensorwerte
✅ Implementiere Store-and-Forward fuer Netzwerkausfaelle
✅ Nutze strukturierte MQTT Topics (ISA-95 / Sparkplug B)
✅ Sichere alle Verbindungen mit TLS und Zertifikaten
✅ Implementiere Watchdog-Timer fuer kritische Aktoren
✅ Verwende Docker auf Edge-Gateways fuer Reproduzierbarkeit
✅ Trenne IT- und OT-Netzwerke (Network Segmentation)
✅ Logge strukturiert mit device_id, timestamp, severity
✅ Versioniere Firmware und Konfigurationen (OTA-fähig)

## Anti-Patterns

❌ Sensor-Rohdaten ohne Vorverarbeitung an die Cloud senden
❌ IP-Adressen, Credentials oder Device-IDs hardcoden
❌ QoS 0 fuer kritische Steuerungsbefehle verwenden
❌ Kein Fallback / Safe-State bei Kommunikationsverlust
❌ Cloud-APIs mit hoher Frequenz vom Edge pollen
❌ Secrets im Klartext auf Edge-Devices speichern
❌ Zeitsynchronisation (NTP/PTP) ignorieren
❌ Keine Datenpufferung bei Broker-Unerreichbarkeit
❌ Monolithische Edge-Applikation ohne Modularisierung
❌ Sensor-Kalibrierung und Drift ignorieren

## Example Prompts

"Designe eine MQTT Topic-Struktur fuer eine Fabrik mit 3 Produktionslinien und 50 Sensoren pro Linie"

"Implementiere einen Revolution Pi Datenerfassungsservice der DIO-Inputs liest und per MQTT publiziert"

"Erstelle ein Siemens S7-1500 Gateway das DB-Werte liest und ueber MQTT an InfluxDB weiterleitet"

"Designe eine Predictive-Maintenance-Pipeline die Vibrationsanomalien an Foerderbandmotoren erkennt"

"Baue einen Beckhoff TwinCAT ADS-Bridge der PLC-Variablen mit einem Cloud Digital Twin synchronisiert"

"Erstelle eine Edge Data Pipeline mit Plausibilitaetschecks, Aggregation und Store-and-Forward"

## References

- [Eclipse Mosquitto](https://mosquitto.org/) — Open Source MQTT Broker
- [EMQX](https://www.emqx.io/) — Enterprise MQTT Platform
- [Revolution Pi](https://revolutionpi.com/) — Industrial Raspberry Pi
- [Kunbus](https://www.kunbus.com/) — RevPi Hersteller
- [OPC Foundation](https://opcfoundation.org/) — OPC UA Standard
- [Sparkplug B](https://sparkplug.eclipse.org/) — MQTT Topic Specification
- [IEC 62443](https://www.iec.ch/) — Industrial Cybersecurity
- [Beckhoff TwinCAT](https://www.beckhoff.com/twincat/) — PC-based Control
- [Siemens TIA Portal](https://www.siemens.com/tia-portal) — PLC Engineering
- [InfluxDB](https://www.influxdata.com/) — Time Series Database
- [Grafana](https://grafana.com/) — Monitoring & Dashboards
- [Node-RED](https://nodered.org/) — Flow-based Programming
