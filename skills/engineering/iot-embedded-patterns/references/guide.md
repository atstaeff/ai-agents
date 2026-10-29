# Device, gateway and control boundaries

Read only the affected hardware or protocol section. Establish the actual device,
firmware/toolchain, timing budget and available test equipment before choosing an API.
A desktop gateway example is not a real-time controller or a certified safety function.

## Sensor and actuator contracts

Represent a reading with sensor identity, units, value, acquisition time and quality.
Keep missing, stale, out-of-range and failed values distinct from a valid zero. Specify
calibration, plausibility range, clock source and freshness at the consumer boundary.
Use monotonic elapsed time for local deadlines; wall-clock corrections must not silently
change a control timeout.

Separate hardware adapters from deterministic validation and control rules. Bound
allocations, queue sizes and work per ISR/task/cycle. Keep blocking I/O, logging and
network waits outside a hard timing path; test the deadline on the intended hardware.

For an actuator command, define source authority, permitted state, range, expiry,
operation identity and acknowledgment of actual execution. A software proxy checking
interlocks does not establish functional safety. Use the site's validated controller,
interlocks and commissioning procedure; preserve the accountable safety owner's boundary.

## MQTT topics and delivery

A simple illustrative hierarchy is site/line/device/channel, with separate telemetry,
status, command and command-result channels. Match existing topic/schema conventions,
ACLs and versioning. A similar hierarchy is not Sparkplug compliance; use the actual
[Sparkplug specification](https://sparkplug.eclipse.org/) when required.

Choose QoS from acceptable loss and duplicate behavior, broker/client support and cost:

| QoS | Transport meaning | Application responsibility |
| --- | --- | --- |
| 0 | At most once between sender and receiver | Tolerate missing updates; detect stale data |
| 1 | At least once | Handle duplicate messages safely |
| 2 | Exactly once within the MQTT delivery exchange | Still define durable processing, external side effects and restart recovery |

MQTT QoS does not guarantee exactly-once physical actuation or an atomic database write.
Use stable command identity, expiry, authorization and a durable result/reconciliation
contract. Retained command topics and session replay can deliver old intent; explicitly
control retention and reject stale commands. Use per-device/topic access controls and
the deployment's supported TLS/identity mechanism.

The [OASIS MQTT specification](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html)
defines these delivery semantics. Check the installed protocol version and client/broker
configuration before relying on session expiry, message expiry or other features.

## Store and forward

1. Persist a bounded pending record before claiming durable acceptance. Include stable
   message identity, schema, acquisition time, destination and required delivery semantics.
2. Publish a bounded batch and wait for the delivery acknowledgment promised by the
   transport/client. A publish call returning or queueing locally is not necessarily
   broker acceptance; inspect the actual client API.
3. Mark the record delivered durably only at that defined point. A crash after broker
   acceptance and before local marking can replay a duplicate; design consumer handling.
4. Distinguish broker delivery from successful business processing where the contract
   requires an application acknowledgment. Preserve failed outcomes for reconciliation.
5. Bound disk use, record age, retry rate and poison-message handling. Define overflow
   policy and signal data loss; cleanup must not delete undelivered data silently.

Exercise offline acquisition, full disk/queue, reconnect, restart during acknowledgment
and duplicate replay. A memory queue does not establish restart durability.

## PLC and protocol mapping

Derive the tag/register map from the actual authorized device export. Record type,
address convention, byte/word order, scale, units, access mode and sampling period.
Do not reuse fictional offsets or assume a generic module's I/O count.

| Integration | Confirm | Failure behavior |
| --- | --- | --- |
| S7 | CPU/access configuration and DB/tag layout | Detect layout change, timeout and invalid reads |
| ADS | Route, target identity and symbol types | Reconnect and refresh invalidated handles |
| OPC UA | Endpoint trust, node IDs and subscription limits | Report bad quality, stale data and reconnect gaps |
| Modbus | Function, device address and register convention | Handle exception response, timeout and invalid range |
| Revolution Pi | Configured modules and process-image ownership | Detect stale samples and restart state |

Start with read-only discovery. Keep PLC scan timing and command ownership separate
from gateway polling; a cloud outage must follow the agreed local-control behavior.
Protocol choice alone does not establish determinism: verify device, bus, topology,
configuration and worst-case load against the actual deadline.

## Control and update recovery

For a closed loop, define sample period, sensor validity, saturation, anti-windup,
startup/reset and the validated safe response. Keep telemetry and remote setpoint changes
within explicit bounds. Bench checks and a Python PID example cannot establish machine safety.

For firmware/configuration updates, verify authenticity and compatible hardware/schema,
define interruption recovery and retain the known-good version where the device supports
it. Test power/network loss at the relevant stage under the site's authorized procedure.

Return the exact target/revision, changed behavior, measured bench/device results and
remaining timing, hardware or safety limits. Use the relevant vendor manual and
[OPC Foundation](https://opcfoundation.org/), [Beckhoff](https://infosys.beckhoff.com/),
[Siemens](https://support.industry.siemens.com/) or [Revolution Pi](https://revolutionpi.com/)
for model-specific facts; do not claim standards compliance from these patterns.
