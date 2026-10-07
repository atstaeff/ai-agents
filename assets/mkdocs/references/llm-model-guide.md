# Choose models by the task

Model names, availability and pricing change. This catalog deliberately avoids a
hardcoded provider/model table. Check your provider's current official documentation
when a decision depends on cost, context limits, tool support or data handling.

| Work | Evaluate |
| --- | --- |
| Routine implementation | Correctness on the actual stack, latency and tool reliability |
| Architecture and difficult debugging | Reasoning quality, relevant context and evidence handling |
| Independent review | Concrete defect detection and low false-positive rate |
| Personal knowledge work | Privacy configuration, language quality and source preservation |

Start with a model already configured in your host. Evaluate a few representative
tasks with the same acceptance criteria and record outcomes, latency and actual cost.
Use a more capable model where a demonstrated failure or difficult decision justifies
it. Do not assign a supposedly cheap model to all implementation without checking it.

Configure model choices in your host, not in every portable agent. Preserve the user
and project's requirements for provider access and sensitive data.
