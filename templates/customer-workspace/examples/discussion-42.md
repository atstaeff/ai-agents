# Example question, response and resumption

Entirely fictional dialogue, provided for format. No messages were sent.

## Jorg to Product Owner, in issue 42

A retry of the same upload attempt should reuse its document reference. A deliberate new
upload of the same PDF should create a new reference. I recommend an attempt key rather
than global file deduplication. Does this match the business meaning of a new submission?

## Example Product Owner reply

Yes. Retrying one attempt must keep the reference. A deliberate new submission may create
another case, even if the PDF is identical.

## Jorg to Operations, in the same issue

What retry window must the portal support after a lost response? This determines attempt-key
retention and behavior after expiry. I can inspect the existing client recovery behavior and
prepare the change while this decision is pending; final acceptance depends on your answer.

## Working update

Preserve the reply as source feedback. Update the bounded issue section with the confirmed
meaning, unresolved retry window, next action and real evidence. Keep the issue Blocked if
that answer prevents the next complete increment; otherwise continue independent work.
Do not repeatedly notify the same contact without a material change or an agreed reminder rule.
