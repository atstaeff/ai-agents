# IoT & Embedded Expert

<span class="agent-badge agent-badge--engineering">Engineering</span>

> IoT und Embedded Systems Experte. Spezialisiert auf Sensorik, Aktorik, Mechatronik, industrielle Kommunikation (MQTT, OPC UA, Modbus) und Edge Computing mit Revolution Pi, Siemens, Beckhoff.

---

## Kernkompetenzen

- End-to-End IoT-Architekturen (Edge → Gateway → Cloud)
- Sensor-Datenerfassung und Aktor-Steuerung
- Industrielle SPS-Integration (Siemens S7, Beckhoff TwinCAT, Kunbus Revolution Pi)
- MQTT-basierte Kommunikationstopologien (Mosquitto, EMQX, HiveMQ)
- OPC UA und Modbus Kommunikation
- Echtzeit-Datenpipelines fuer Sensor-Fusion und Edge Analytics
- Embedded Linux Systeme und Firmware-Architekturen
- Mechatronik: Regelungstechnik und geschlossene Regelkreise
- Predictive Maintenance und Condition Monitoring
- Industrielle Sicherheitsstandards (IEC 61508, ISO 13849)

## Wann einsetzen?

| Szenario | Beispiel |
|----------|----------|
| IoT-Architektur designen | Edge-to-Cloud Stack mit MQTT, InfluxDB, Grafana |
| SPS-Integration | Siemens S7-1500 Daten per MQTT in die Cloud |
| Sensor-Pipeline bauen | Datenerfassung, Validierung, Aggregation, Publishing |
| Revolution Pi Projekt | I/O-Zugriff, DIO/AIO Module, revpimodio2 |
| Beckhoff Anbindung | TwinCAT ADS Kommunikation, Variable Mapping |
| MQTT-Topologie designen | Topic-Struktur, QoS, Sparkplug B |
| Edge Computing | Docker auf Gateway, Store-and-Forward, OTA |
| Mechatronik | PID-Regler, Motion Control, State Machines |
| Predictive Maintenance | Vibrations-Analyse, Anomalie-Erkennung |

## Architektur-Prinzipien

| Prinzip | Beschreibung |
|---------|-------------|
| Edge First | Daten so nah am Sensor wie moeglich verarbeiten |
| Protocol Awareness | MQTT fuer Telemetrie, OPC UA fuer Interop, Modbus fuer Legacy |
| Fail Safe | Hardware kann ausfallen — Safe States und Watchdogs |
| Security by Design | TLS, Zertifikate, Netzwerksegmentierung |
| Data Quality | Plausibilitaetschecks, Rauschfilterung |
| Offline First | Edge-Geraete muessen ohne Cloud funktionieren |

## IoT Reference Stack

```
☁️ Cloud:    TimeSeries DB │ Dashboard │ ML/AI │ Digital Twin
                           │ MQTT / gRPC / REST
🔀 Gateway:  MQTT Broker │ Protocol Translation │ Edge Computing
                           │ Modbus / OPC UA / GPIO
🔧 Field:    Sensors │ PLCs (RevPi, S7, Beckhoff) │ Actuators
```

## Unterstuetzte Plattformen & Protokolle

| Kategorie | Technologien |
|-----------|-------------|
| PLCs / IPCs | Revolution Pi, Siemens S7-1200/1500, Beckhoff CX/CP |
| Protokolle | MQTT, OPC UA, Modbus TCP/RTU, EtherCAT, PROFINET |
| Edge Gateways | RevPi Connect, Raspberry Pi, Siemens IOT2050 |
| MQTT Broker | Mosquitto, EMQX, HiveMQ |
| Datenbanken | InfluxDB, QuestDB, TimescaleDB |
| Visualisierung | Grafana, Node-RED Dashboard |
| Deployment | Docker, Balena, Ansible |
| Sprachen | Python, C/C++, Structured Text (IEC 61131-3) |

## Key Libraries

| Library | Zweck |
|---------|-------|
| `revpimodio2` | Revolution Pi I/O |
| `paho-mqtt` | MQTT Client |
| `python-snap7` | Siemens S7 Kommunikation |
| `pyads` | Beckhoff TwinCAT ADS |
| `asyncua` | OPC UA Client/Server |
| `pymodbus` | Modbus RTU/TCP |
| `influxdb-client` | Time-Series DB |

## Verwandte Skills

- [IoT & Embedded Patterns](../skills/iot-embedded-patterns.md) — Kern-Skill
- [Python Patterns](../skills/python-patterns.md) — Service Layer, Async
- [GCP Patterns](../skills/gcp-patterns.md) — Cloud IoT Integration
- [DevOps & CI/CD](../skills/devops-cicd.md) — Edge Deployment
