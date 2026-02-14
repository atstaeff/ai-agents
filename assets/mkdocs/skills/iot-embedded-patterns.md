# IoT & Embedded Patterns

> IoT und Embedded Patterns: MQTT, OPC UA, Modbus, Sensorik, Aktorik, Revolution Pi, Siemens S7, Beckhoff TwinCAT, Edge Computing und Mechatronik.

---

## Kernpatterns

### Sensor Abstraction Layer

- Hardware-agnostische Sensor-Interfaces (Protocol pattern)
- SensorReading mit Quality-Flag (good, uncertain, bad, out_of_range)
- Plausibilitaetschecks: Range, Rate-of-Change, Stuck-at Detection
- Sliding Window Aggregation (Mean, StdDev, Min, Max)

### Actuator Command Pattern

- Safe Actuator Proxy mit Interlock-Checks
- State Machine: DISABLED → STANDBY → RUNNING → FAULT
- Watchdog Timer fuer kritische Aktoren
- Audit Trail fuer alle Steuerungsbefehle

### MQTT Communication

- Hierarchische Topic-Struktur (ISA-95 / Sparkplug B)
- QoS-Auswahl: 0 fuer High-Frequency, 1 fuer Standard, 2 fuer kritisch
- TLS und Zertifikat-basierte Authentifizierung
- Last Will & Testament fuer Device-Offline-Detection
- Store-and-Forward bei Netzwerkausfaellen

### Protocol Gateway

- Abstraction ueber industrielle Protokolle
- Tag-Mapping: PLC-Variable → MQTT Topic
- Deadband-Filterung (nur bei signifikanter Aenderung publizieren)
- Polling-basiert oder Event-driven (ADS Notifications)

### Edge Data Pipeline

- Pipeline: Acquire → Validate → Aggregate → Transform → Publish
- Offline-faehig mit SQLite-basiertem Message Buffer
- Containerisiert mit Docker / Docker Compose
- Health Monitoring: CPU, Memory, Disk, Sensor Status

## Industrielle Plattformen

### Revolution Pi (Kunbus)

- piControl Interface (`/dev/piControl0`)
- revpimodio2 High-Level Library
- Module: DIO (Digital), AIO (Analog), MIO (Mixed), Gateway
- Cyclic Processing mit konfigurierbarer Zykluszeit
- Safe-State Handling bei Shutdown

### Siemens S7

- snap7 / python-snap7 fuer S7-300/400/1200/1500
- Datenbaustein-Zugriff (DB Read/Write)
- Datentypen: BOOL, INT, REAL, STRING
- Rack/Slot-basierte Verbindung

### Beckhoff TwinCAT

- pyads fuer ADS-Kommunikation
- Symbolischer Variablenzugriff (`MAIN.fTemperature`)
- ADS Notifications fuer Event-driven Updates
- TwinCAT 3 Runtime (Port 851)

### OPC UA

- asyncua / python-opcua
- Node-basierter Zugriff mit Namespaces
- Security Policies (Basic256Sha256)
- Browse, Read, Write, Subscribe

### Modbus

- pymodbus fuer TCP und RTU
- Register Types: Holding, Input, Coils, Discrete Inputs
- Unit-ID basierte Adressierung
- Serial (RS485) und TCP Varianten

## Protokoll-Auswahl

| Anforderung | Empfohlenes Protokoll |
|-------------|----------------------|
| Cloud Telemetrie | MQTT (QoS 1) |
| Industrielle Interoperabilitaet | OPC UA |
| Legacy-Geraete anbinden | Modbus TCP/RTU |
| Echtzeit Motion Control | EtherCAT |
| Siemens-Oekosystem | PROFINET / S7 |
| Smart Sensors | IO-Link |
| Automotive / Embedded | CANopen |

## IoT Edge Stack (Docker Compose)

| Service | Image | Zweck |
|---------|-------|-------|
| Mosquitto | eclipse-mosquitto:2 | MQTT Broker |
| Node-RED | nodered/node-red | Visual Flow Programming |
| InfluxDB | influxdb:2 | Time-Series Datenbank |
| Grafana | grafana/grafana | Dashboards |
| Telegraf | telegraf | Metrics Collection |
| Edge App | Custom | Datenerfassung & Steuerung |
