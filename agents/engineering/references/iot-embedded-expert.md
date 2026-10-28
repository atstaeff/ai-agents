# Device and industrial integration handoffs

Use the [role](../iot-embedded-expert.agent.md) for a bounded firmware or gateway change.
The [embedded skill](../../../skills/engineering/iot-embedded-patterns/SKILL.md) and its
[guide](../../../skills/engineering/iot-embedded-patterns/references/guide.md) own sensor,
protocol, buffering and control-boundary guidance.

## Establish the physical boundary

Supply board/PLC model, firmware/toolchain, wiring or register/tag map, units, byte order,
sample period, memory/power budget and available test equipment. Identify which outputs
can move equipment and who owns the validated safe state. A gateway or cloud callback
must not silently become the safety controller; identify the applicable site procedure
and competent owner before changing a safety function.

## Protocol-specific evidence

| Boundary | Confirm before implementation | Useful check |
| --- | --- | --- |
| Revolution Pi | Installed module/process-image map and access owner | Read a known input; verify stale-data and restart handling |
| Siemens S7 | CPU mode, authorized connection and exported tag/DB offsets | Validate type, offset and endianness against a known value |
| Beckhoff ADS | Target route, AMS identity and symbol types | Reconnect after route loss; reject a changed symbol layout |
| OPC UA | Endpoint, trust configuration, node identity and subscription limits | Reject an untrusted peer; detect stale or dropped values |
| Modbus | Device address, register convention, function and byte/word order | Exercise timeout, exception response and invalid range |
| MQTT | Broker/session policy, topic ACL, schema and command expiry | Duplicate delivery, reconnect, stale command and full buffer |

Begin read-only when discovering a live device. Keep writes within the assigned scope
and use the site's test/commissioning procedure. Return exact target/revision, changed
behavior, executed bench/device checks and limits; simulations do not establish physical
safety, real-time performance or compliance with an industrial standard.

Follow the installed vendor documentation rather than copying an unverified register
map or library API. Starting points: [Revolution Pi](https://revolutionpi.com/),
[Beckhoff documentation](https://infosys.beckhoff.com/),
[Siemens support](https://support.industry.siemens.com/) and
[OPC Foundation](https://opcfoundation.org/).
