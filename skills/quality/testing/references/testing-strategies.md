# Select a verification strategy

Use this reference when deciding where evidence belongs. The
[focused test guide](guide.md) owns fixture, boundary and execution examples; keep the
strategy tied to the affected product risk rather than a universal test pyramid.

## Choose the cheapest check that observes the risk

Start with the requirement or reproduced defect. Use a unit test for a local rule,
a contract check for serialization/permissions, a real integration check for storage or
network semantics and a running journey for critical interaction. Combine boundaries
when one check cannot establish the criterion. There is no required ratio by test type.

For example, an order total can have deterministic rule cases, a denied cross-customer
request needs authorization evidence and concurrent checkout may need a real transaction
check. A UI click alone may miss a database invariant; a mocked repository may hide it.

## Methods for specific uncertainty

| Method | Useful when | Avoid |
| --- | --- | --- |
| Regression reproduction | A concrete fault can be made observable | A test that passes before the faulty behavior changes |
| Characterization | Legacy behavior must survive a structural change | Treating accidental behavior as a new requirement without review |
| Property-based testing | Many inputs share a clear invariant | Generating data without a meaningful oracle |
| Contract testing | Independently changed consumers/providers share a boundary | Assuming a schema-valid document establishes running compatibility |
| End-to-end journey | Integration or user interaction is the central risk | Duplicating every unit edge case through a slow UI |
| Fault/recovery exercise | Timeout, restart or partial write affects correctness | Simulating a simple exception and calling crash recovery verified |

TDD is useful when it clarifies a rule or reproduces a bug. Choose the workflow that
exposes the real failure; a mandated red/green ritual for a wording edit adds no evidence.

## Evaluate adequacy

Map each important criterion to actual evidence and a revision. Inspect negative and
recovery cases, fixture realism and whether a double hides the boundary under review.
Use established coverage gates where required; a percentage alone does not establish
important behavior or justify additional low-value tests.

Keep the suite deterministic, understandable and fast enough for its feedback loop.
When test maintenance outweighs the risk it observes, narrow the boundary or remove
redundant coverage with an explicit rationale. Report a missing environment as unrun,
not passed or inapplicable.
