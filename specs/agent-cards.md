\# Agent Cards



\## Orchestrator Agent



\### Purpose



The Orchestrator Agent acts as the workflow manager for PharmaAssist AI. It receives user requests, coordinates the execution of specialized agents, determines the next agent to run based on prior results, and ensures the workflow follows the defined business rules and guardrails.



\### Inputs



\* User Request

\* Member Information

\* Drug Information

\* Eligibility Agent Output

\* Coverage Agent Output

\* Recommendation Agent Output

\* Workflow Rules



\### Outputs



\* Next Agent To Execute

\* Workflow Status

\* Final Consolidated Response

\* Workflow Completion Decision

\* Error or Escalation Messages



\### Permissions



\* Read User Inputs

\* Read Agent Outputs

\* Route Requests Between Agents

\* Execute Workflow Rules

\* Trigger Agent Execution

\* Log Workflow Decisions



\### Not Allowed To



\* Modify Eligibility Results

\* Modify Coverage Results

\* Modify Member Information

\* Override Agent Decisions

\* Approve Benefits

\* Submit Claims

\* Change Coverage Data

\* Bypass Guardrails



\### Risk Level



Medium



Reason:

The Orchestrator does not make benefit decisions directly, but it controls the workflow. An incorrect routing decision could lead to skipped validations, unnecessary processing, or incorrect final responses.







\## Eligibility Agent



\### Purpose

Verify whether the member has active coverage on the requested Date of Service under the specified policy or benefit plan.



\### Inputs

Last Name, DOB, Date of Service and Policy Number



\### Outputs

Eligibility Status



Coverage Start Date



Coverage End Date



Eligibility Reason



\### Permissions

Allowed to ready only Eligibility-related information of Start Date and End Date



\### Not Allowed To

Modify/deleted any date



\### Risk Level

Low



\---



\## Coverage Agent



\### Purpose

Coverage agent provides the coverage by looking into the eligibility and covered drugs



\### Inputs

Drug Name, Strength, Quantity, Days Supply



\### Outputs

Coverage Status



PA Required



Coverage Reason



\### Permissions

Should be able to look at the specific drug from the Drug Table



\### Not Allowed To

Modify any data



\### Risk Level

Medium



\---



\## Recommendation Agent



\###Purpose



Analyze the eligibility and coverage results and recommend the next appropriate action for the pharmacy technician or customer service representative.



\###Inputs



Eligibility Status

Coverage Status

Prior Authorization Requirement

Coverage Reason

Drug Information



\###Outputs



Recommended Next Action

Reason for Recommendation

Escalation Required (Yes/No)



\###Permissions



Read Eligibility Results

Read Coverage Results

Read Drug Information

Generate Recommendations



\###Not Allowed To



Modify Eligibility Results

Modify Coverage Results

Approve Prior Authorization

Submit Claims

Change Member Information



\###Risk Level



Medium



\###Reason



Recommendations may influence operational decisions but do not directly modify benefit information.

\---



\## Evaluation Agent



\### Purpose



Review the workflow output, assess confidence, validate completeness, and provide a quality score before the final response is returned.



\###Inputs



Eligibility Result

Coverage Result

Recommendation Result

Workflow Execution Details



\###Outputs



Confidence Score

Evaluation Status

Validation Comments

Final Quality Assessment



\###Permissions



Read Agent Outputs

Evaluate Workflow Results

Generate Quality Scores

Generate Validation Comments



\###Not Allowed To



Modify Agent Outputs

Override Eligibility Decisions

Override Coverage Decisions

Change Recommendations



\###Risk Level



Low



\###Reason



The Evaluation Agent only assesses quality and does not perform business actions.



\## Orchestrator Agent



\### Purpose



Coordinate the pharmacy benefits verification workflow by determining which specialized agents should execute based on the user's request and the results returned by previous agents.



\---



\### Inputs



\- Member ID

\- Date of Service

\- Drug Name



\---



\### Outputs



\- Combined workflow response

\- Workflow status

\- Recommendation



\---



\### Permissions



\- Invoke specialized agents

\- Read structured responses

\- Stop workflow when required



\---



\### Not Allowed To



\- Make eligibility decisions

\- Determine coverage

\- Change business data

\- Modify recommendations



\---



\### Risk Level



Medium



\## Explanation Agent



\## Purpose



Generate a natural language explanation for the business decision returned by the Orchestrator.



\---



\### Inputs



\- Eligibility Result

\- Coverage Result

\- Recommendation

\- Coverage Reason



\---



\### Outputs



\- Human-readable explanation



\---



\### Permissions



\- Read structured response from the Orchestrator

\- Call the Gemini API



\---



\### Not Allowed To



\- Change eligibility

\- Change coverage

\- Change recommendation

\- Modify business data



\---



\### Risk Level



Low





