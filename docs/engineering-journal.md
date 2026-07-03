\# Sprint 3 – Orchestrator Design



\## Sprint Goal



Design and implement an Orchestrator that coordinates specialized agents without embedding business logic.



\## Why



The Orchestrator improves modularity by delegating tasks to specialized agents instead of allowing agents to call each other directly.



\## Design Decision



\* Specialized agents remain loosely coupled.

\* The Orchestrator owns the workflow.

\* Business rules remain deterministic.

\* Agents exchange structured outputs.



\## White Paper Mapping



\* Agent Orchestration

\* Specialized Agents

\* Separation of Concerns

\* Structured Workflows



\## Lessons Learned



An Orchestrator coordinates work but does not perform business operations itself. This keeps the architecture modular and easier to extend.



\# Sprint 3.5 – Refactoring



\## Goal



Improve the communication between agents by replacing string values ("Yes"/"No") with boolean values (True/False).



\---



\## Why



Boolean values are machine-friendly, reduce comparison logic, and provide a consistent contract between agents.



\---



\## Design Decision



\- Converted Coverage Agent to return booleans.

\- Recommendation Agent already consumed booleans.

\- Orchestrator required no changes because it simply passes structured data between agents.



\---



\## White Paper Mapping



\- Structured Outputs

\- Reliable Agent Communication

\- Deterministic Business Logic

\- Separation of Concerns



\---



\## Lessons Learned



Agents should exchange structured machine-readable data instead of human-readable values. Human-readable explanations should be generated separately by the LLM.

