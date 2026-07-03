\# Pharmacy Benefits Verification Workflow



\## User Goal



Determine whether a member can receive a requested medication and identify the next business action.



\---



\## Workflow Steps



\### Step 1

Invoke the Eligibility Agent.



If the member is not eligible:

\- Stop the workflow.

\- Return the eligibility result.



\---



\### Step 2

Invoke the Coverage Agent.



Determine:

\- Drug Coverage

\- Prior Authorization Requirement



\---



\### Step 3

Invoke the Recommendation Agent.



Determine the next business action based on:

\- Eligibility

\- Coverage

\- Prior Authorization



\---



\### Step 4

Return one structured response containing:

\- Eligibility

\- Coverage

\- Recommendation

\- Workflow Status

