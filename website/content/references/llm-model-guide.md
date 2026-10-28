# Choose models by the task

Configure model choices in the host. Use its current official documentation and your
provider's documentation for availability, pricing, context limits, tools and data handling.
The [runtime guide](../getting-started/installation.md) links adapter sources; portable
profiles do not prescribe a provider or a fixed model hierarchy.

| Work | Evaluate |
| --- | --- |
| Bounded implementation | Correctness on the actual stack, latency and tool reliability |
| Architecture and difficult debugging | Reasoning quality, relevant context and evidence handling |
| Independent review | Concrete defect detection and low false-positive rate |
| Personal knowledge work | Privacy configuration, language quality and source preservation |

Start with an available model and representative tasks using the same acceptance
criteria. Record accepted results, review effort, failures, latency and actual cost.
Try economical specialists on bounded work; use a more capable model where evidence
or a difficult decision justifies it. A lower price per call alone does not establish
lower cost per accepted result.

Keep credentials and private settings out of exported catalog sources. Herd packages
contain no model-routing keys. The [orchestration guide](../getting-started/orchestration.md)
describes leader and specialist responsibilities; the host owns their actual model settings.
