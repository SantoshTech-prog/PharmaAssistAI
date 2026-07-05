
\# 🏥 PharmaAssist AI



\## A Specification-Driven Multi-Agent Pharmacy Benefits Verification System



PharmaAssist AI is a \*\*Specification-Driven Multi-Agent AI application\*\* that automates pharmacy benefits verification by combining deterministic business logic with \*\*Google Gemini\*\* for natural language explanations.



Rather than relying on a single Large Language Model (LLM), this project demonstrates how specialized AI agents, coordinated by an Orchestrator, can solve complex business workflows in a reliable, explainable, and maintainable manner.



This project was developed as part of the \*\*Kaggle AI Agents Intensive Capstone\*\* and demonstrates modern AI Engineering principles including:



\- Specification-Driven Development (SDD)

\- Multi-Agent Architecture

\- Context Engineering

\- AI + Tools + Guardrails

\- Deterministic Business Logic

\- AI Evaluation



\---



\## 🚀 Project Highlights



\- 🤖 Specification-Driven Multi-Agent Architecture

\- 🎯 Orchestrator-Based Workflow Coordination

\- 📐 Human-Readable Agent Specifications

\- ⚙️ Deterministic Business Logic using Python

\- 💬 Google Gemini for Natural Language Explanations

\- 🛡 AI + Tools + Guardrails Design Pattern

\- 📊 AI Evaluation and Quality Validation

\- 🖥 Interactive Streamlit Dashboard



\---



\# 📑 Table of Contents



Executive Summary

Problem Statement

Specification-Driven Development

Multi-Agent Architecture

Context Engineering

AI + Tools + Guardrails

Why Google Gemini Is Only Used for Explanation

Evaluation

Solution Architecture



\# 📖 Executive Summary



PharmaAssist AI demonstrates how modern AI applications can be built using a \*\*Specification-Driven Development (SDD)\*\* approach instead of relying on a single monolithic AI prompt.



The application simulates a real-world pharmacy benefits verification workflow by dividing responsibilities across multiple specialized agents. Each agent performs a single deterministic task, while the Orchestrator coordinates the workflow and ensures that the right agent is executed at the right time.



Google Gemini is intentionally used only where natural language reasoning adds value—explaining structured decisions to end users. All business decisions remain deterministic and are implemented in Python, making the system reliable, predictable, and easy to validate.



This architecture demonstrates how AI can complement traditional software engineering rather than replace it.



\# 🎯 Problem Statement



Pharmacy benefits verification is a common workflow performed by healthcare providers, pharmacies, and insurance companies before dispensing prescription medications. The objective is to determine whether a prescribed medication is covered under a member's health plan and identify any additional requirements before the medication can be approved.



A typical pharmacy benefits verification process involves answering questions such as:



\- Is the member currently eligible for benefits?

\- Is the requested medication covered by the benefit plan?

\- Does the medication require Prior Authorization?

\- What action should the provider take next?

\- How can the decision be explained clearly to the patient or provider?



Traditionally, these questions are answered by consulting multiple systems, business rules, and policy documents. This often requires manual effort, increases processing time, and can lead to inconsistent explanations.



\---



\## Challenges



A straightforward approach might be to send all of the available information to a Large Language Model (LLM) and ask it to determine the outcome. However, this introduces several challenges:



\- LLMs should not be responsible for deterministic business decisions.

\- Business rules require consistency and repeatability.

\- Eligibility and coverage decisions must be traceable and explainable.

\- AI-generated responses should never replace validated business logic.

\- Large prompts increase cost, latency, and the likelihood of hallucinations.



For these reasons, relying solely on an LLM is not an appropriate architecture for business-critical healthcare workflows.



\---



\## Engineering Objective



The objective of this project is not simply to automate pharmacy benefits verification.



Instead, the goal is to demonstrate how modern AI Engineering principles can be applied to build a reliable, modular, and explainable system by:



\- Separating deterministic business logic from AI reasoning.

\- Using specialized agents instead of a single monolithic AI prompt.

\- Coordinating the workflow through an Orchestrator.

\- Applying Specification-Driven Development (SDD).

\- Using AI only where natural language reasoning provides value.



This approach produces a solution that is easier to maintain, easier to test, easier to extend, and significantly more reliable than an LLM-only implementation.



\# 📐 Specification-Driven Development (SDD)



One of the primary objectives of this project was to follow a \*\*Specification-Driven Development (SDD)\*\* approach, an AI engineering practice emphasized throughout the Kaggle AI Agents Intensive course.



Instead of immediately writing Python code, each major component of the system was first defined through a human-readable specification describing:



\- The agent's responsibility

\- Expected inputs

\- Expected outputs

\- Decision boundaries

\- Interaction with other agents

\- Success criteria



These specifications served as the blueprint for implementation, ensuring that every component had a clearly defined purpose before development began.



\---



\## Development Workflow



The project followed the workflow below:



```text

Business Requirements

\\\\\\\&#x20;         │

\\\\\\\&#x20;         ▼

\\\\\\\&#x20;  Specifications

\\\\\\\&#x20;         │

\\\\\\\&#x20;         ▼

\\\\\\\&#x20;    Agent Cards

\\\\\\\&#x20;         │

\\\\\\\&#x20;         ▼

\\\\\\\&#x20; Python Implementation

\\\\\\\&#x20;         │

\\\\\\\&#x20;         ▼

\\\\\\\&#x20;Unit Testing \\\\\\\\\\\\\\\& Validation

\\\\\\\&#x20;         │

\\\\\\\&#x20;         ▼

\\\\\\\&#x20;Orchestrator Integration

\\\\\\\&#x20;         │

\\\\\\\&#x20;         ▼

\\\\\\\&#x20;Streamlit User Interface

```



Each phase builds upon the previous one, reducing ambiguity and encouraging modular system design.



\---



\## Agent-First Design



Rather than designing the application around a single AI model, the system was designed around \*\*specialized agents\*\*, each with one clearly defined responsibility.



The following agent specifications were created before implementation:



| Agent | Primary Responsibility |

|--------|------------------------|

| Eligibility Agent | Verify member eligibility |

| Coverage Agent | Determine drug coverage |

| Recommendation Agent | Generate the next business action |

| Explanation Agent | Produce a natural language explanation using Google Gemini |

| Evaluation Agent | Validate the quality and consistency of the AI-generated explanation |

| Orchestrator | Coordinate the workflow between specialized agents |



Each agent follows the \*\*Single Responsibility Principle\*\*, making the system easier to understand, test, and extend.



\---



\## Why Specification-Driven Development?



Building AI systems without specifications often leads to tightly coupled components, unclear responsibilities, and unpredictable behavior.



By adopting Specification-Driven Development, this project achieved several engineering benefits:



\- Improved modularity

\- Clear separation of responsibilities

\- Easier testing and validation

\- Simplified maintenance

\- Better scalability

\- Reduced implementation ambiguity

\- Consistent interaction between agents



Most importantly, specifications became the source of truth throughout the development lifecycle, allowing implementation to remain aligned with the original design.



\---



\## Project Structure



To reinforce the Specification-Driven Development approach, specifications were maintained separately from implementation.



```text

PharmaAssistAI/



├── specs/

│   ├── orchestrator\\\\\\\\\\\\\\\_agent.md

│   ├── explanation\\\\\\\\\\\\\\\_agent.md

│   ├── evaluation\\\\\\\\\\\\\\\_agent.md

│   └── ...

│

├── agents/

│   ├── eligibility\\\\\\\\\\\\\\\_agent.py

│   ├── coverage\\\\\\\\\\\\\\\_agent.py

│   ├── recommendation\\\\\\\\\\\\\\\_agent.py

│   ├── explanation\\\\\\\\\\\\\\\_agent.py

│   └── evaluation\\\\\\\\\\\\\\\_agent.py

```



This separation ensures that architecture, design decisions, and implementation evolve independently while remaining aligned.



\# 🤖 Multi-Agent Architecture



Rather than solving the entire pharmacy benefits verification workflow using a single Large Language Model (LLM), PharmaAssist AI adopts a \*\*Multi-Agent Architecture\*\* where each agent is responsible for one well-defined task.



Each agent operates independently, performs a single responsibility, and returns structured output to the Orchestrator. This design improves reliability, modularity, and maintainability while making the system easier to extend as new business requirements emerge.



\---



\## Why Multi-Agent Architecture?



As business workflows grow in complexity, assigning all responsibilities to a single AI model creates several challenges:



\- Large prompts become difficult to manage.

\- AI models may perform deterministic business decisions inconsistently.

\- Individual responsibilities become tightly coupled.

\- Testing and debugging become more difficult.

\- Extending the workflow often requires rewriting existing logic.



Instead, PharmaAssist AI decomposes the workflow into specialized agents that collaborate through an Orchestrator.



This approach follows a core principle of modern AI Engineering:



> \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\*\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\*Build many small experts rather than one large generalist.\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\*\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\*



\---



\## Current Agent Responsibilities



| Agent | Responsibility | Type |

|--------|----------------|------|

| Eligibility Agent | Determines whether the member is eligible for pharmacy benefits | Deterministic |

| Coverage Agent | Determines whether the requested medication is covered | Deterministic |

| Recommendation Agent | Determines the next business action based on eligibility and coverage | Deterministic |

| Explanation Agent | Generates a natural language explanation using Google Gemini | AI |

| Evaluation Agent | Validates the AI-generated explanation against structured business decisions | AI Evaluation |

| Orchestrator | Coordinates workflow execution and aggregates responses | Coordinator |



Each agent has a \*\*single responsibility\*\*, allowing it to evolve independently without impacting the rest of the system.



\---



\## Role of the Orchestrator



The Orchestrator acts as the central coordinator of the workflow.



Its responsibilities include:



\- Receiving the user request

\- Building the execution plan

\- Executing agents in the correct order

\- Passing structured data between agents

\- Handling early termination when required

\- Returning a unified response to the user



Importantly, the Orchestrator \*\*does not implement business logic\*\*.



Instead, it delegates decision-making to specialized agents while ensuring that each agent executes only when required.



\---



\## Agent Collaboration



The workflow implemented in PharmaAssist AI follows the sequence below.



```text

User Request

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\&#x20;     │

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\&#x20;     ▼

Orchestrator

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\&#x20;     │

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\&#x20;     ▼

Eligibility Agent

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\&#x20;     │

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\&#x20;     ▼

Coverage Agent

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\&#x20;     │

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\&#x20;     ▼

Recommendation Agent

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\&#x20;     │

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\&#x20;     ▼

Explanation Agent

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\&#x20;     │

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\&#x20;     ▼

Evaluation Agent

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\&#x20;     │

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\&#x20;     ▼

Final Response

```



Each agent receives only the information required to perform its responsibility and returns structured output to the Orchestrator.



Agents never invoke one another directly.



\---



\## Extensibility



One of the primary advantages of a Multi-Agent Architecture is extensibility.



For example, suppose the business introduces a new requirement:



> Verify whether the prescribing physician is part of the insurance network.



Rather than modifying existing agents, the system can be extended by introducing a new \*\*Network Agent\*\*.



```text

User Request

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\&#x20;     │

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\&#x20;     ▼

Orchestrator

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\&#x20;     │

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\&#x20;     ├────────► Eligibility Agent

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\&#x20;     ├────────► Coverage Agent

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\&#x20;     ├────────► Network Agent

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\&#x20;     ├────────► Recommendation Agent

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\&#x20;     ├────────► Explanation Agent

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\&#x20;     └────────► Evaluation Agent

```



The existing agents remain unchanged.



Only the Orchestrator is updated to include the new agent in the workflow.



This demonstrates one of the key principles of Specification-Driven Development:



> \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\*\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\*Extend the system by adding specialized agents rather than modifying existing ones.\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\*\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\*



\---



\## Benefits of This Architecture



The Multi-Agent Architecture provides several engineering advantages:



\- Improved modularity

\- Clear separation of responsibilities

\- Easier unit testing

\- Simplified maintenance

\- Better scalability

\- Lower coupling between components

\- Easier onboarding for new developers

\- Ability to replace or upgrade individual agents independently



Most importantly, this architecture enables deterministic business logic and AI reasoning to coexist while remaining clearly separated.



This separation makes the system more reliable, explainable, and maintainable than an architecture built around a single LLM prompt.



\# ⚙️ Context Engineering



One of the most important AI Engineering principles demonstrated in this project is \*\*Context Engineering\*\*.



Large Language Models (LLMs) perform best when provided with focused, relevant, and structured information. Instead of sending the entire application state or large amounts of unnecessary data, PharmaAssist AI carefully constructs the minimum context required for the model to perform its task.



This improves response quality while reducing cost, latency, and the risk of hallucinations.



\---



\## What is Context Engineering?



Context Engineering is the practice of designing \*\*what information is sent to an AI model\*\*, \*\*how it is structured\*\*, and \*\*why it is included\*\*.



Rather than asking an LLM to determine business decisions, the system first performs all deterministic processing using specialized agents.



Only after those decisions have been made is a carefully constructed prompt sent to Google Gemini.



This ensures that the LLM receives only the information required to generate a clear, natural language explanation.



\---



\## Context Flow



The Explanation Agent does not communicate directly with Google Gemini.



Instead, it delegates responsibilities across dedicated components.



```text

Structured Business Decisions

           │

           ▼

     Prompt Builder

           │

           ▼

  Optimized AI Prompt
           │

           ▼

     Gemini Client

           │

           ▼

    Google Gemini API

           │

           ▼

Natural Language Explanation

```



Each component has a single responsibility:



| Component | Responsibility |

|-----------|----------------|

| Explanation Agent | Coordinates explanation generation |

| Prompt Builder | Builds the minimum required prompt |

| Gemini Client | Handles communication with Google Gemini |

| Google Gemini | Generates the natural language explanation |



This layered approach keeps the system modular and easy to maintain.



\---



\## Why Build a Prompt Builder?



Rather than embedding prompts directly inside the Explanation Agent, PharmaAssist AI introduces a dedicated \*\*Prompt Builder\*\*.



The Prompt Builder is responsible for:



\- Selecting only relevant business information

\- Formatting structured data into a consistent prompt

\- Excluding unnecessary context

\- Keeping prompt construction separate from AI communication



Separating prompt construction from AI communication makes both components easier to test, maintain, and replace independently.



\---



\## Minimum Context Principle



One of the guiding principles of this project is:



> \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\*\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\*Give the AI only the minimum information it needs to perform its task.\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\*\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\*



For example, Google Gemini receives information such as:



\- Eligibility status

\- Coverage status

\- Prior Authorization requirement

\- Coverage reason

\- Recommended business action



It does \*\*not\*\* receive:



\- CSV files

\- Internal business rules

\- Complete application state

\- Agent implementation details

\- Unrelated workflow information



By limiting context to only what is necessary, the model produces more focused and consistent explanations.



\---



\## Benefits of Context Engineering



Applying Context Engineering provides several engineering advantages:



\- Reduced prompt size

\- Lower inference cost

\- Faster response times

\- Reduced hallucination risk

\- Improved consistency

\- Better prompt maintainability

\- Easier testing and debugging

\- Greater model portability



Most importantly, Context Engineering ensures that AI complements deterministic software instead of replacing it.



\---



\## Why This Matters



Many AI applications simply send all available data to an LLM and expect it to determine the outcome.



PharmaAssist AI follows a different approach.



Business decisions are made by deterministic agents using predefined rules.



Only the final, validated decisions are sent to Google Gemini, whose sole responsibility is to transform structured information into a human-readable explanation.



This demonstrates how Context Engineering can be used to build AI systems that are more reliable, maintainable, and aligned with modern AI engineering best practices.







\# 🛡️ AI + Tools + Guardrails



One of the central architectural patterns demonstrated in PharmaAssist AI is the \*\*AI + Tools + Guardrails\*\* design pattern.



Instead of asking a Large Language Model (LLM) to perform every task, responsibilities are divided between deterministic software components and AI, with validation mechanisms ensuring the final response remains accurate, reliable, and explainable.



This approach combines the strengths of traditional software engineering with modern AI capabilities.



\---



\## What is AI + Tools + Guardrails?



The pattern divides responsibilities into three distinct layers.



\### 🤖 AI



AI is responsible only for tasks that require natural language generation or reasoning.



In PharmaAssist AI, Google Gemini is used exclusively to transform structured business decisions into clear, human-readable explanations.



AI is \*\*not responsible\*\* for making business decisions.



\---



\### ⚙️ Tools



Tools perform deterministic business logic using predefined rules.



These tools always produce the same output for the same input, making them reliable, predictable, and easy to validate.



The deterministic tools implemented in PharmaAssist AI include:



\- Eligibility Agent

\- Coverage Agent

\- Recommendation Agent



These agents execute Python business logic rather than relying on AI reasoning.



\---



\### 🛡️ Guardrails



Guardrails ensure that AI operates within well-defined boundaries.



Rather than allowing AI to determine eligibility, coverage, or recommendations, the system constrains the model to explaining decisions that have already been made.



Guardrails also validate AI-generated output before it is presented to the user.



The guardrails implemented in PharmaAssist AI include:



\- Specification-Driven Development

\- Structured business rules

\- Orchestrator-controlled workflow

\- Prompt Builder with minimum required context

\- Evaluation Agent for response validation

\- Separation of deterministic logic from AI reasoning



These mechanisms reduce hallucinations while improving reliability and explainability.



\---



\## How PharmaAssist AI Implements This Pattern



The following diagram illustrates how the three components collaborate.



```text

\\\&#x20;                   USER REQUEST

\\\&#x20;                         │

\\\&#x20;                         ▼

\\\&#x20;                 Orchestrator

\\\&#x20;                         │

\\\&#x20;         ┌───────────────┴───────────────┐

\\\&#x20;         ▼                               ▼

\\\&#x20;   Deterministic Tools              AI Reasoning

\\\&#x20;         │                               │

\\\&#x20;         │                               ▼

Eligibility Agent                 Explanation Agent

Coverage Agent                           │

Recommendation Agent                     ▼

\\\&#x20;         │                       Prompt Builder

\\\&#x20;         │                               │

\\\&#x20;         ▼                               ▼

\\\&#x20; Structured Decisions            Google Gemini

\\\&#x20;         │                               │

\\\&#x20;         └───────────────┬───────────────┘

\\\&#x20;                         ▼

\\\&#x20;                 Evaluation Agent

\\\&#x20;                         │

\\\&#x20;                         ▼

\\\&#x20;                 Final User Response

```



\---



\## Why This Architecture?



This architecture intentionally limits the responsibility of AI.



Business-critical decisions remain deterministic and are implemented using Python, while AI focuses exclusively on improving the user experience through natural language explanations.



This separation provides several engineering benefits:



\- Reliable business decisions

\- Explainable AI responses

\- Easier testing

\- Reduced hallucination risk

\- Clear separation of responsibilities

\- Improved maintainability

\- Better regulatory alignment for business workflows



\---



\## Key Design Decision



One of the most important architectural decisions in this project is:



> \\\\\\\*\\\\\\\*Google Gemini never determines business outcomes.\\\\\\\*\\\\\\\*



Instead, Gemini receives only validated, structured business decisions and converts them into clear explanations for end users.



This ensures that AI enhances communication without replacing deterministic software engineering.



\---



\## Engineering Takeaway



The AI + Tools + Guardrails pattern demonstrates that successful AI systems are not built by replacing software with AI.



Instead, they are built by combining deterministic software, specialized AI capabilities, and architectural guardrails into a cohesive, reliable system.



PharmaAssist AI applies this pattern throughout its architecture, resulting in a system that is modular, explainable, maintainable, and aligned with modern AI engineering best practices.





\# 💬 Why Google Gemini Is Only Used for Explanation



One of the most important architectural decisions in PharmaAssist AI was intentionally limiting the role of Google Gemini.



Rather than using AI to perform every task within the application, Google Gemini is used exclusively to generate natural language explanations for decisions that have already been made by deterministic business logic.



This separation was a deliberate engineering decision designed to maximize reliability while still benefiting from modern Large Language Models (LLMs).



\---



\## The Design Decision



During the design phase, several possible approaches were considered.



\### Option 1 — AI Determines Everything ❌



```text

User Request

\\\&#x20;     │

\\\&#x20;     ▼

\\\&#x20;Google Gemini

\\\&#x20;     │

\\\&#x20;     ▼

Eligibility

Coverage

Recommendation

Explanation

```



Although this approach appears simple, it introduces several engineering risks:



\- Business decisions become non-deterministic.

\- Responses may vary for identical inputs.

\- Business rules become difficult to validate.

\- Hallucinations may affect critical healthcare decisions.

\- Testing and debugging become significantly more difficult.



For these reasons, this architecture was intentionally rejected.



\---



\### Option 2 — Deterministic Business Logic + AI Explanation ✅



```text

User Request

\\\&#x20;     │

\\\&#x20;     ▼

Deterministic Agents

\\\&#x20;     │

\\\&#x20;     ▼

Structured Business Decision

\\\&#x20;     │

\\\&#x20;     ▼

Google Gemini

\\\&#x20;     │

\\\&#x20;     ▼

Natural Language Explanation

```



This architecture separates decision-making from explanation generation.



Business decisions remain deterministic and fully traceable, while AI focuses solely on communicating those decisions in clear, user-friendly language.



This is the architecture implemented in PharmaAssist AI.



\---



\## Why Only Explanation?



Natural language explanation is an ideal use case for a Large Language Model because it requires:



\- Converting structured data into conversational language

\- Improving readability for end users

\- Summarizing technical business decisions

\- Explaining outcomes in a consistent, understandable manner



Unlike eligibility or coverage determination, explanation does not change the underlying business outcome.



This makes it a safe and valuable application of AI.



\---



\## Responsibilities



The system deliberately separates responsibilities between deterministic software and AI.



| Responsibility | Implemented By |

|---------------|----------------|

| Member Eligibility | Eligibility Agent |

| Drug Coverage | Coverage Agent |

| Prior Authorization Logic | Coverage Agent |

| Business Recommendation | Recommendation Agent |

| Workflow Coordination | Orchestrator |

| Natural Language Explanation | Google Gemini |

| Explanation Validation | Evaluation Agent |



This clear separation keeps the architecture modular and predictable.



\---



\## Engineering Benefits



Restricting Google Gemini to explanation generation provides several advantages:



\- Deterministic business decisions

\- Reduced hallucination risk

\- Easier testing and validation

\- Improved explainability

\- Lower operational risk

\- Simpler maintenance

\- Clear separation of concerns

\- Easier replacement of the underlying LLM in the future



Because the Explanation Agent communicates with Gemini through the Prompt Builder and Gemini Client, the underlying language model can be replaced with another provider (such as OpenAI, Anthropic, or a self-hosted model) with minimal impact on the rest of the application.



\---



\## Alignment with Modern AI Engineering



Modern AI systems should not delegate every responsibility to an LLM.



Instead, AI should be applied selectively where it adds the greatest value.



PharmaAssist AI follows this principle by combining deterministic software engineering with AI-generated explanations.



This demonstrates a practical application of the \*\*AI + Tools + Guardrails\*\* pattern, where:



\- \*\*Tools\*\* make business decisions.

\- \*\*AI\*\* explains those decisions.

\- \*\*Guardrails\*\* ensure the AI operates within clearly defined boundaries.



This design results in a system that is reliable, explainable, maintainable, and aligned with modern AI engineering best practices.





\# 📊 Evaluation



One of the defining characteristics of modern AI Engineering is recognizing that \*\*an AI-generated response should not automatically be considered correct simply because it was generated by a Large Language Model (LLM).\*\*



For this reason, PharmaAssist AI introduces a dedicated \*\*Evaluation Agent\*\* that validates AI-generated explanations before they are presented to the user.



Rather than assuming the explanation is accurate, the system verifies that it is consistent with the structured business decisions produced earlier in the workflow.



This additional validation layer demonstrates a responsible approach to AI system design.



\---



\## Why Evaluate AI Responses?



Large Language Models are powerful at generating natural language, but they can occasionally:



\- Omit important information

\- Introduce unsupported statements

\- Misrepresent structured business decisions

\- Produce inconsistent explanations

\- Hallucinate information that was never provided



In business-critical domains such as healthcare, these risks make evaluation an essential part of the workflow.



\---



\## Evaluation Workflow



After the Explanation Agent generates the natural language response, the Evaluation Agent compares it with the deterministic business decisions.



```text

Structured Business Decisions

\\\&#x20;           │

\\\&#x20;           ▼

\\\&#x20;    Explanation Agent

\\\&#x20;           │

\\\&#x20;           ▼

\\\&#x20;Google Gemini Explanation

\\\&#x20;           │

\\\&#x20;           ▼

\\\&#x20;     Evaluation Agent

\\\&#x20;           │

\\\&#x20;           ▼

\\\&#x20;Quality Assessment

\\\&#x20;           │

\\\&#x20;           ▼

\\\&#x20;    Final User Response

```



This ensures that the explanation accurately reflects the validated business outcome.



\---



\## Responsibilities of the Evaluation Agent



The Evaluation Agent is responsible for:



\- Reviewing AI-generated explanations

\- Comparing explanations with structured business decisions

\- Measuring explanation quality

\- Identifying inconsistencies

\- Reporting evaluation results



The Evaluation Agent \*\*does not modify the explanation\*\*.



Its responsibility is to evaluate and report on the quality of the generated response.



\---



\## Evaluation Criteria



Within PharmaAssist AI, the Evaluation Agent validates whether the explanation correctly represents:



\- Member eligibility

\- Drug coverage status

\- Prior Authorization requirement

\- Coverage reason

\- Recommended business action



These checks ensure that the explanation remains aligned with the deterministic business logic executed by earlier agents.



\---



\## Evaluation Output



The Evaluation Agent returns structured metadata that summarizes the quality of the explanation.



Typical evaluation results include:



| Field | Description |

|--------|-------------|

| Passed | Whether the explanation is consistent with the structured decision |

| Quality Score | Overall evaluation score |

| Summary | Human-readable evaluation summary |

| Issues | List of inconsistencies or observations |



This structured output is displayed within the Streamlit application to provide transparency into the quality of the AI-generated explanation.



\---



\## Why a Separate Evaluation Agent?



Evaluation is intentionally implemented as an independent agent rather than being embedded within the Explanation Agent.



This design follows the \*\*Single Responsibility Principle\*\*.



\- The Explanation Agent generates explanations.

\- The Evaluation Agent validates explanations.



Separating these responsibilities makes the system easier to test, maintain, and extend.



For example, future versions of the system could introduce:



\- Multiple evaluation strategies

\- Domain-specific evaluation rules

\- Automatic quality thresholds

\- Human review workflows

\- Continuous AI quality monitoring



without modifying the Explanation Agent itself.



\---



\## Engineering Benefits



Introducing a dedicated Evaluation Agent provides several advantages:



\- Increased confidence in AI-generated responses

\- Improved explainability

\- Better quality assurance

\- Reduced operational risk

\- Easier debugging

\- Clear separation of responsibilities

\- Stronger alignment with responsible AI practices



Most importantly, evaluation transforms the AI response from an assumed answer into a verified output.



\---



\## Alignment with Modern AI Engineering



Modern AI systems should not stop after generating a response.



Instead, they should include mechanisms to assess the quality and reliability of AI outputs before they reach end users.



By introducing a dedicated Evaluation Agent, PharmaAssist AI demonstrates an important AI engineering principle:



> \\\\\\\*\\\\\\\*Generation should be followed by evaluation.\\\\\\\*\\\\\\\*



This additional layer improves trust, transparency, and reliability while reinforcing the AI + Tools + Guardrails architecture implemented throughout the system.



\# 🏗️ Solution Architecture



PharmaAssist AI is designed as a layered, specification-driven, multi-agent system where each layer has a clearly defined responsibility.



Instead of embedding business logic inside an LLM, deterministic processing and AI reasoning are intentionally separated into different architectural layers.



This design improves reliability, maintainability, explainability, and scalability.



\---



\## High-Level Architecture



```text

\\\\\\\\\\\\\\\&#x20;                       User

\\\\\\\\\\\\\\\&#x20;                         │

\\\\\\\\\\\\\\\&#x20;                         ▼

\\\\\\\\\\\\\\\&#x20;                Streamlit Web Application

\\\\\\\\\\\\\\\&#x20;                         │

\\\\\\\\\\\\\\\&#x20;                         ▼

\\\\\\\\\\\\\\\&#x20;                   Orchestrator

\\\\\\\\\\\\\\\&#x20;                         │

\\\\\\\\\\\\\\\&#x20;       ┌─────────────────┼─────────────────┐

\\\\\\\\\\\\\\\&#x20;       ▼                 ▼                 ▼

\\\\\\\\\\\\\\\&#x20;Eligibility Agent   Coverage Agent   Recommendation Agent

\\\\\\\\\\\\\\\&#x20;                         │

\\\\\\\\\\\\\\\&#x20;                         ▼

\\\\\\\\\\\\\\\&#x20;                Explanation Agent

\\\\\\\\\\\\\\\&#x20;                         │

\\\\\\\\\\\\\\\&#x20;                 Prompt Builder

\\\\\\\\\\\\\\\&#x20;                         │

\\\\\\\\\\\\\\\&#x20;                         ▼

\\\\\\\\\\\\\\\&#x20;                  Gemini Client

\\\\\\\\\\\\\\\&#x20;                         │

\\\\\\\\\\\\\\\&#x20;                         ▼

\\\\\\\\\\\\\\\&#x20;                 Google Gemini API

\\\\\\\\\\\\\\\&#x20;                         │

\\\\\\\\\\\\\\\&#x20;                         ▼

\\\\\\\\\\\\\\\&#x20;                Evaluation Agent

\\\\\\\\\\\\\\\&#x20;                         │

\\\\\\\\\\\\\\\&#x20;                         ▼

\\\\\\\\\\\\\\\&#x20;                 Final User Response

```



\---



\## Layered Architecture



The system is organized into multiple layers, each responsible for a specific aspect of the workflow.



\### 1. Presentation Layer



The Streamlit application provides a simple and interactive interface where users can:



\- Enter member information

\- Submit a pharmacy benefit verification request

\- View recommendations

\- Read AI-generated explanations

\- Review evaluation results



The presentation layer contains \*\*no business logic\*\*.



\---



\### 2. Orchestration Layer



The Orchestrator is the central coordinator of the application.



Its responsibilities include:



\- Receiving the user request

\- Planning the execution workflow

\- Invoking specialized agents

\- Managing execution order

\- Stopping the workflow when required

\- Aggregating responses into a single output



The Orchestrator never performs business decisions itself.



\---



\### 3. Business Logic Layer



This layer contains deterministic Python agents responsible for business decisions.



Current agents include:



\- Eligibility Agent

\- Coverage Agent

\- Recommendation Agent



These agents execute predefined business rules and always produce consistent outputs for the same inputs.



No AI reasoning is performed in this layer.



\---



\### 4. AI Reasoning Layer



The Explanation Agent is the only component that interacts with Google Gemini.



Instead of making business decisions, its responsibility is to convert structured business outcomes into clear, human-readable explanations.



To improve reliability and reduce unnecessary context, the Explanation Agent delegates work to two additional components:



\- Prompt Builder

\- Gemini Client



This separation improves maintainability and allows the underlying LLM to be replaced with minimal changes.



\---



\### 5. Evaluation Layer



After the explanation is generated, the Evaluation Agent verifies that the AI response is consistent with the structured business decisions produced earlier in the workflow.



This additional validation step improves confidence in AI-generated outputs and demonstrates responsible AI engineering practices.



\---



\## Architectural Principles



Several software engineering principles guided the design of this architecture.



| Principle | Implementation |

|-----------|----------------|

| Single Responsibility | Each agent performs exactly one task |

| Separation of Concerns | UI, orchestration, business logic, and AI are isolated |

| Loose Coupling | Agents never directly invoke one another |

| High Cohesion | Related functionality remains within each agent |

| Modularity | Components can be replaced independently |

| Extensibility | New agents can be added with minimal changes |

| Testability | Individual agents can be tested independently |

| Explainability | Every business decision can be explained in natural language |



These principles ensure that the system remains maintainable as additional business capabilities and AI agents are introduced.





\# 📁 Project Structure



The repository is organized to reflect the principles of \*\*Specification-Driven Development (SDD)\*\* and \*\*Multi-Agent Architecture\*\*. Each directory has a clearly defined responsibility, making the project modular, maintainable, and easy to extend.



```text

PharmaAssistAI/

│

├── agents/

│   ├── eligibility\_agent.py

│   ├── coverage\_agent.py

│   ├── recommendation\_agent.py

│   ├── explanation\_agent.py

│   └── evaluation\_agent.py

│

├── ai/

│   ├── prompt\_builder.py

│   └── gemini\_client.py

│

├── data/

│   ├── members.csv

│   └── drug\_formulary.csv

│

├── specs/

│   ├── orchestrator\_agent.md

│   ├── eligibility\_agent.md

│   ├── coverage\_agent.md

│   ├── recommendation\_agent.md

│   ├── explanation\_agent.md

│   └── evaluation\_agent.md

│

├── tests/

│

├── app.py

├── orchestrator.py

├── requirements.txt

├── README.md

└── .gitignore

```



\---



\## Repository Organization



\### 📂 agents/



Contains the specialized agents responsible for performing individual tasks within the pharmacy benefits verification workflow.



Each agent follows the \*\*Single Responsibility Principle\*\*, ensuring that it performs exactly one business function.



Current agents include:



\- Eligibility Agent

\- Coverage Agent

\- Recommendation Agent

\- Explanation Agent

\- Evaluation Agent



\---



\### 📂 ai/



Contains reusable AI-related components.



Rather than embedding prompt generation or API communication inside business agents, AI responsibilities are separated into dedicated modules.



Current components include:



\- \*\*Prompt Builder\*\* – Constructs the minimum context sent to Google Gemini.

\- \*\*Gemini Client\*\* – Handles communication with the Google Gemini API.



This separation makes the AI layer easier to maintain and allows the underlying language model to be replaced with minimal changes.



\---



\### 📂 data/



Contains sample datasets used by the deterministic agents.



For this demonstration project, CSV files simulate backend healthcare systems such as:



\- Member eligibility records

\- Drug formulary information



In a production implementation, these files would typically be replaced by enterprise databases or external APIs.



\---



\### 📂 specs/



Contains the human-readable specifications created before implementation.



Each specification defines:



\- Agent responsibilities

\- Inputs

\- Outputs

\- Decision boundaries

\- Success criteria



These specifications serve as the blueprint for implementation, reflecting the project's Specification-Driven Development approach.



\---



\### 📂 tests/



Reserved for automated unit and integration tests.



As the project evolves, this directory can include:



\- Unit tests for individual agents

\- Integration tests for orchestrated workflows

\- Regression tests

\- AI evaluation tests



Separating tests from implementation promotes maintainability and continuous quality assurance.



\---



\### 📄 app.py



The Streamlit application that provides the user interface for interacting with PharmaAssist AI.



It allows users to:



\- Enter member information

\- Select a medication

\- Execute the workflow

\- View recommendations

\- Read AI-generated explanations

\- Review evaluation results



\---



\### 📄 orchestrator.py



The central coordination component of the application.



The Orchestrator is responsible for:



\- Receiving user requests

\- Building the execution plan

\- Invoking specialized agents

\- Managing workflow execution

\- Aggregating results into a unified response



The Orchestrator coordinates the workflow but does not perform business decisions.



\---



\### 📄 requirements.txt



Lists all Python dependencies required to run the application.



Installing these dependencies ensures that the development environment matches the project's expected runtime configuration.



\---



\### 📄 README.md



Provides comprehensive project documentation, including:



\- Business context

\- AI engineering principles

\- System architecture

\- Installation instructions

\- Usage guidance

\- Future enhancements



The README serves as both technical documentation and a portfolio case study demonstrating modern AI engineering practices.



\# 🚀 Installation



Follow the steps below to set up PharmaAssist AI on your local machine.



\---



\## Prerequisites



Before installing the project, ensure the following software is available:



\- Python 3.10 or later

\- Git

\- A Google AI Studio API Key (Gemini)



\---



\## Step 1 – Clone the Repository



Clone the project from GitHub.



```bash

git clone https://github.com/<your-username>/PharmaAssistAI.git

cd PharmaAssistAI

```



> Replace `<your-username>` with your GitHub username after publishing the repository.



\---



\## Step 2 – Create a Virtual Environment



Creating a virtual environment keeps project dependencies isolated from other Python projects.



\### Windows



```bash

python -m venv .venv

.venv\\Scripts\\activate

```



\### macOS / Linux



```bash

python3 -m venv .venv

source .venv/bin/activate

```



After activation, your terminal should display the virtual environment name.



Example:



```text

(.venv)

```



\---



\## Step 3 – Install Project Dependencies



Install all required Python packages.



```bash

pip install -r requirements.txt

```



The required packages include:



\- Streamlit

\- Google Generative AI SDK

\- Python Dotenv

\- Pandas



along with any additional project dependencies listed in `requirements.txt`.



\---



\## Step 4 – Configure the Google Gemini API Key



Create a file named:



```text

.env

```



in the root directory of the project.



Add your Google Gemini API key:



```text

GOOGLE\_API\_KEY=your\_google\_gemini\_api\_key

```



Replace:



```text

your\_google\_gemini\_api\_key

```



with your own API key obtained from Google AI Studio.



> \*\*Important:\*\* Never commit your `.env` file or API keys to source control.



\---



\## Step 5 – Verify the Installation



Ensure the following files are present:



```text

PharmaAssistAI/

│

├── app.py

├── orchestrator.py

├── requirements.txt

├── .env

│

├── agents/

├── ai/

├── specs/

├── data/

└── tests/

```



Your virtual environment should also be activated before running the application.



\---



\## Installation Complete



Once the dependencies are installed and the API key is configured, the application is ready to run.



The next section explains how to launch the Streamlit application and interact with PharmaAssist AI.



\# ▶️ Running the Application



After completing the installation and configuring your Google Gemini API key, you are ready to launch PharmaAssist AI.



\---



\## Step 1 – Activate the Virtual Environment



If your virtual environment is not already activated, activate it before running the application.



\### Windows



```bash

.venv\\Scripts\\activate

```



\### macOS / Linux



```bash

source .venv/bin/activate

```



Your terminal should display the virtual environment name.



Example:



```text

(.venv)

```



\---



\## Step 2 – Start the Streamlit Application



Run the following command from the project root directory:



```bash

streamlit run app.py

```



If the application starts successfully, Streamlit will display output similar to:



```text

You can now view your Streamlit app in your browser.



Local URL: http://localhost:8501

Network URL: http://192.xxx.xxx.xxx:8501

```



Open the \*\*Local URL\*\* in your web browser.



\---



\## Step 3 – Use the Application



The Streamlit interface allows you to simulate a pharmacy benefits verification request.



Enter the required information:



\- \*\*Member ID\*\*

\- \*\*Date of Service\*\*

\- \*\*Drug Name\*\*



Example:



| Field | Example Value |

|-------|---------------|

| Member ID | 1001 |

| Date of Service | 2026-05-01 |

| Drug Name | Ozempic |



Click the \*\*Verify Pharmacy Benefit\*\* button to start the workflow.



\---



\## Step 4 – Workflow Execution



When a request is submitted, the Orchestrator coordinates the execution of the specialized agents in sequence.



```text

User Request

&#x20;     │

&#x20;     ▼

Orchestrator

&#x20;     │

&#x20;     ▼

Eligibility Agent

&#x20;     │

&#x20;     ▼

Coverage Agent

&#x20;     │

&#x20;     ▼

Recommendation Agent

&#x20;     │

&#x20;     ▼

Explanation Agent

&#x20;     │

&#x20;     ▼

Evaluation Agent

&#x20;     │

&#x20;     ▼

Final Response

```



Each agent performs a single responsibility and returns structured output to the Orchestrator.



\---



\## Step 5 – Review the Results



After the workflow completes, the application displays:



\- Member eligibility status

\- Drug coverage status

\- Prior Authorization requirement

\- Recommended business action

\- AI-generated explanation (Google Gemini)

\- Evaluation results



This demonstrates how deterministic business logic and AI-generated explanations work together within a coordinated multi-agent system.



\---



\## Expected Output



A successful execution produces results similar to the following:



```text

Eligibility Status:

✔ Eligible



Coverage Status:

✔ Covered



Prior Authorization:

Required



Recommendation:

Submit Prior Authorization Request



AI Explanation:

The member is eligible for pharmacy benefits, and the requested medication is covered under the plan. However, Prior Authorization is required before the medication can be approved. The provider should submit the required documentation for review.



Evaluation:

✔ Passed

Quality Score: High

```



> \*\*Note:\*\* The explanation generated by Google Gemini may vary slightly between executions, while the deterministic business decisions remain consistent.



\---



\## Troubleshooting



\### ModuleNotFoundError



Install missing dependencies:



```bash

pip install -r requirements.txt

```



\---



\### Missing Google API Key



Ensure that a `.env` file exists in the project root and contains:



```text

GOOGLE\_API\_KEY=your\_google\_gemini\_api\_key

```



\---



\### Streamlit Does Not Start



Verify that:



\- The virtual environment is activated.

\- All dependencies are installed.

\- `app.py` is located in the project root.

\- The required Python version is installed.



\---



\## Next Steps



After confirming that the application runs successfully, explore the remaining sections of this README to learn about the system architecture, AI engineering principles, and opportunities for future enhancements.



\# 📸 Application Screenshots



The following screenshots illustrate the end-to-end workflow of PharmaAssist AI.



These examples demonstrate how deterministic business logic, AI-powered explanations, and evaluation work together through a coordinated multi-agent architecture.



\---



\## 🏠 Home Screen



The Streamlit home page allows users to initiate a pharmacy benefits verification request.



Users provide:



\- Member ID

\- Date of Service

\- Drug Name



The Orchestrator then coordinates the execution of the specialized agents.



> \*\*Screenshot Placeholder\*\*



```text

screenshots/home\_page.png

```



\---



\## 🤖 Agent Execution Workflow



After submitting a request, the Orchestrator invokes each specialized agent in sequence.



The workflow includes:



\- Eligibility Agent

\- Coverage Agent

\- Recommendation Agent

\- Explanation Agent

\- Evaluation Agent



This demonstrates how the application coordinates multiple agents while maintaining clear separation of responsibilities.



> \*\*Screenshot Placeholder\*\*



```text

screenshots/agent\_workflow.png

```



\---



\## 💊 Pharmacy Benefits Verification Result



Once processing is complete, the application displays the structured business outcome, including:



\- Eligibility Status

\- Coverage Status

\- Prior Authorization Requirement

\- Recommended Business Action



These results are produced by deterministic business logic implemented in Python.



> \*\*Screenshot Placeholder\*\*



```text

screenshots/business\_result.png

```



\---



\## 💬 AI-Generated Explanation



Google Gemini receives the validated business decisions and generates a clear, human-readable explanation.



The Explanation Agent is responsible only for natural language generation and does not perform business decision-making.



> \*\*Screenshot Placeholder\*\*



```text

screenshots/gemini\_explanation.png

```



\---



\## 📊 Evaluation Results



The Evaluation Agent reviews the AI-generated explanation and validates that it accurately represents the deterministic business decisions.



Displayed information may include:



\- Evaluation Status

\- Quality Score

\- Summary

\- Validation Results



This additional verification step demonstrates responsible AI engineering practices.



> \*\*Screenshot Placeholder\*\*



```text

screenshots/evaluation\_result.png

```



\---



\## 🏗️ Complete Application Flow



The following image illustrates the overall user experience from request submission through final response.



```text

User

&#x20;  │

&#x20;  ▼

Streamlit

&#x20;  │

&#x20;  ▼

Orchestrator

&#x20;  │

&#x20;  ▼

Eligibility Agent

&#x20;  │

&#x20;  ▼

Coverage Agent

&#x20;  │

&#x20;  ▼

Recommendation Agent

&#x20;  │

&#x20;  ▼

Explanation Agent

&#x20;  │

&#x20;  ▼

Evaluation Agent

&#x20;  │

&#x20;  ▼

Final Response

```



> \*\*Screenshot Placeholder\*\*



```text

screenshots/complete\_workflow.png

```



\---



\## Repository Screenshots Folder



Store all application images in the following directory:



```text

PharmaAssistAI/

│

├── screenshots/

│   ├── home\_page.png

│   ├── agent\_workflow.png

│   ├── business\_result.png

│   ├── gemini\_explanation.png

│   ├── evaluation\_result.png

│   └── complete\_workflow.png

```



Keeping screenshots in a dedicated directory makes the repository easier to maintain and ensures all image references remain organized.



\# 🔮 Future Enhancements



PharmaAssist AI was intentionally designed using a modular, specification-driven, multi-agent architecture. This design allows new capabilities to be added by introducing specialized agents rather than modifying existing ones.



The following enhancements represent potential future directions for the project.



\---



\## 🤖 Additional Specialized Agents



The current implementation demonstrates the core pharmacy benefits verification workflow. Future versions can expand the system by introducing additional domain-specific agents.



\### Network Verification Agent



Verify whether the prescribing physician or pharmacy is part of the member's insurance network.



\*\*Potential Responsibilities\*\*



\- Validate provider network status

\- Identify out-of-network providers

\- Suggest in-network alternatives



\---



\### Formulary Agent



Determine the medication's formulary tier and identify preferred alternatives.



\*\*Potential Responsibilities\*\*



\- Verify formulary placement

\- Recommend preferred medications

\- Identify generic alternatives

\- Detect non-formulary drugs



\---



\### Claims History Agent



Analyze previous pharmacy claims to support coverage decisions.



\*\*Potential Responsibilities\*\*



\- Retrieve historical claims

\- Detect duplicate prescriptions

\- Identify refill patterns

\- Support utilization review



\---



\### Appeals Agent



Assist providers when coverage is denied.



\*\*Potential Responsibilities\*\*



\- Explain denial reasons

\- Generate appeal guidance

\- Recommend supporting documentation

\- Track appeal status



\---



\### Clinical Guidelines Agent



Evaluate prescriptions against evidence-based clinical guidelines.



Potential future capabilities include:



\- Clinical rule validation

\- Treatment pathway recommendations

\- Guideline references

\- Drug interaction awareness



\---



\## 🌐 Enterprise Integrations



The current project uses CSV files to simulate backend systems.



Future versions could integrate with:



\- Healthcare databases

\- REST APIs

\- FHIR-compliant systems

\- Electronic Health Records (EHR)

\- Pharmacy Benefit Manager (PBM) platforms

\- Insurance provider systems



These integrations would allow the application to operate with real-time healthcare data.



\---



\## 🧠 Advanced AI Capabilities



Future AI enhancements may include:



\- Retrieval-Augmented Generation (RAG) for policy and formulary retrieval

\- Multi-model support (Google Gemini, OpenAI, Anthropic)

\- Human-in-the-loop review workflows

\- AI-powered document summarization

\- Natural language query support

\- Personalized explanation generation



These capabilities would further enhance the flexibility and usability of the system.



\---



\## 📊 Enhanced Evaluation



The Evaluation Agent can be extended with more sophisticated quality assurance capabilities.



Potential improvements include:



\- LLM-as-a-Judge evaluation

\- Automatic quality scoring

\- Consistency validation across multiple models

\- Hallucination detection

\- Explainability metrics

\- Human review checkpoints



These enhancements would strengthen confidence in AI-generated responses.



\---



\## 📈 Observability and Monitoring



Production-ready AI systems require comprehensive monitoring.



Future enhancements may include:



\- Agent execution metrics

\- Workflow tracing

\- API performance monitoring

\- Prompt version tracking

\- AI response analytics

\- Error dashboards

\- Logging and audit trails



These capabilities would improve operational visibility and simplify troubleshooting.



\---



\## 🚀 Deployment Enhancements



Future deployment options include:



\- Docker containerization

\- Kubernetes orchestration

\- CI/CD pipelines using GitHub Actions

\- Cloud deployment on Google Cloud, AWS, or Azure

\- Secure secrets management

\- Auto-scaling infrastructure



These enhancements would support enterprise-grade deployments.



\---



\## 🔐 Security and Compliance



Future versions can incorporate additional security features such as:



\- OAuth authentication

\- Role-based access control (RBAC)

\- API authentication

\- Encryption of sensitive data

\- Secure secrets management

\- Audit logging

\- HIPAA-aligned security practices for healthcare environments



\---



\## 📱 User Experience Improvements



Potential user interface enhancements include:



\- Interactive workflow visualization

\- Dark mode support

\- Searchable verification history

\- Downloadable PDF reports

\- Export to CSV

\- Mobile-responsive design

\- Accessibility improvements



\---



\## Long-Term Vision



The long-term vision for PharmaAssist AI is to evolve from a demonstration project into a production-ready AI platform capable of supporting real-world healthcare workflows.



By following the principles of Specification-Driven Development, Multi-Agent Architecture, Context Engineering, and AI + Tools + Guardrails, the system can continue to grow through the addition of specialized agents while maintaining reliability, explainability, and modularity.



This extensible architecture ensures that future capabilities can be introduced with minimal impact on existing components, making PharmaAssist AI well-positioned for enterprise-scale AI engineering.



\# 🎓 Lessons Learned



Developing PharmaAssist AI was more than building a healthcare demonstration project—it was an opportunity to apply modern AI engineering principles to a realistic business workflow.



Throughout the project, several important technical and architectural lessons emerged.



\---



\## 1. AI Is Most Effective When Combined with Software Engineering



One of the biggest takeaways from this project is that successful AI applications are not built by replacing software with Large Language Models.



Instead, the most reliable systems combine deterministic software engineering with AI capabilities.



In PharmaAssist AI:



\- Python performs deterministic business decisions.

\- Google Gemini generates natural language explanations.

\- The Evaluation Agent validates AI-generated responses.



This separation creates a system that is both reliable and explainable.



\---



\## 2. Specification-Driven Development Reduces Complexity



Designing specifications before writing code significantly improved the development process.



Creating agent specifications first made it easier to:



\- Define clear responsibilities.

\- Reduce implementation ambiguity.

\- Maintain consistency across components.

\- Build each agent independently.



The specifications became the blueprint for implementation and helped keep the architecture aligned with the original design.



\---



\## 3. Multi-Agent Systems Scale Better Than Monolithic AI Solutions



Breaking the workflow into specialized agents proved to be more effective than relying on a single AI prompt.



Each agent performs one responsibility:



\- Eligibility verification

\- Coverage determination

\- Recommendation generation

\- Explanation generation

\- Evaluation



This modular approach improves maintainability, testability, and future extensibility.



\---



\## 4. Context Engineering Improves AI Reliability



Providing only the minimum required context to Google Gemini resulted in clearer and more focused explanations.



Rather than exposing the entire application state to the language model, only validated business decisions were included in the prompt.



This approach:



\- Reduces hallucination risk

\- Improves consistency

\- Lowers token usage

\- Simplifies prompt maintenance



\---



\## 5. AI Should Explain Decisions, Not Make Them



One of the most important architectural decisions in this project was restricting Google Gemini to explanation generation.



Business decisions remain deterministic and are implemented using Python.



This separation reinforces the principle that AI should enhance user communication while business logic remains predictable and verifiable.



\---



\## 6. Evaluation Is an Essential Part of AI Systems



Generating an AI response should not be considered the final step.



Introducing a dedicated Evaluation Agent demonstrated how AI-generated outputs can be validated before reaching the end user.



This additional layer increases confidence in the system and aligns with responsible AI engineering practices.



\---



\## 7. Modular Architecture Enables Future Growth



The project was intentionally designed to accommodate future enhancements without requiring major architectural changes.



New business capabilities can be introduced by adding specialized agents while keeping existing components unchanged.



This demonstrates the long-term value of modular, loosely coupled system design.



\---



\## 8. Documentation Is Part of Engineering



A well-designed system should be understandable not only through its code but also through its documentation.



Preparing this README reinforced the importance of documenting:



\- Business context

\- Architectural decisions

\- AI engineering principles

\- System design

\- Development approach



Comprehensive documentation improves maintainability, collaboration, and knowledge sharing.



\---



\## Personal Reflection



This project significantly strengthened my understanding of modern AI engineering beyond simply integrating a Large Language Model into an application.



Through designing and implementing PharmaAssist AI, I gained practical experience in:



\- Specification-Driven Development (SDD)

\- Multi-Agent Architecture

\- Context Engineering

\- AI + Tools + Guardrails

\- Orchestrator-based workflows

\- Responsible AI design

\- AI evaluation techniques



More importantly, this project reinforced that building production-quality AI systems requires thoughtful software engineering, clear architectural decisions, and disciplined system design—not just effective prompting.



\---



\## Final Takeaway



PharmaAssist AI demonstrates that the future of AI engineering lies in combining deterministic software, specialized AI capabilities, and well-defined architectural patterns.



By applying principles such as Specification-Driven Development, Multi-Agent Architecture, Context Engineering, and AI + Tools + Guardrails, this project illustrates how AI can be integrated into business workflows in a way that is reliable, explainable, maintainable, and extensible.



The knowledge gained from this project provides a strong foundation for building more advanced AI systems capable of addressing increasingly complex real-world challenges.



\# 🏁 Conclusion



PharmaAssist AI demonstrates that modern AI applications are most effective when they combine traditional software engineering principles with the strengths of Large Language Models.



By applying Specification-Driven Development, Multi-Agent Architecture, Context Engineering, AI + Tools + Guardrails, and AI Evaluation, this project illustrates a practical approach to building AI systems that are reliable, explainable, maintainable, and extensible.



Rather than replacing deterministic software with AI, PharmaAssist AI shows how AI can be integrated thoughtfully into enterprise workflows to improve communication while preserving consistency, transparency, and trust.



The architecture presented in this project provides a strong foundation for extending the system with additional agents, enterprise integrations, and production-ready capabilities, demonstrating how modern AI engineering principles can be applied to solve real-world business problems.



\# 👨‍💻 About the Author



Hi, I'm \*\*Santosh Kumar\*\*, an IT professional with over \*\*14 years of experience\*\* in software quality assurance, product ownership, application support, and digital transformation. Throughout my career, I have worked on enterprise-scale solutions across the healthcare, aviation, and information technology domains, with a strong focus on delivering reliable, user-centric software.



As AI continues to reshape software development, I have been actively expanding my expertise in \*\*AI Engineering\*\*, \*\*Large Language Models (LLMs)\*\*, \*\*Multi-Agent Systems\*\*, \*\*Specification-Driven Development (SDD)\*\*, and \*\*Context Engineering\*\*. My goal is to build AI-powered applications that combine the reliability of traditional software engineering with the capabilities of modern generative AI.



PharmaAssist AI was developed as part of the \*\*Kaggle AI Agents Intensive Capstone\*\* to demonstrate how modern AI engineering principles can be applied to a realistic healthcare workflow. Rather than relying solely on an LLM, the project showcases how deterministic software, specialized AI agents, orchestration, and evaluation can work together to build reliable, explainable, and maintainable AI systems.



This project reflects my belief that the future of AI lies not in replacing software engineering, but in combining disciplined engineering practices with intelligent systems to solve real-world business problems.



\---



\## 📬 Connect With Me



I welcome feedback, discussions, and collaboration on AI Engineering, Multi-Agent Systems, Software Architecture, and Healthcare Technology.



\- \*\*GitHub:\*\* https://github.com/<your-github-username>

\- \*\*LinkedIn:\*\* https://www.linkedin.com/in/<your-linkedin-profile>

\- \*\*Email:\*\* <your-email-address>



> \*"Great AI systems are not built by prompts alone—they are engineered through thoughtful architecture, clear specifications, deterministic software, and responsible use of AI."\*

