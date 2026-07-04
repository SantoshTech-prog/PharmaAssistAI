from agents.evaluation_agent import evaluate_explanation
from agents.explanation_agent import explain_decision
from agents.eligibility_agent import check_eligibility
from agents.coverage_agent import check_coverage
from agents.recommendation_agent import get_recommendation


def process_pharmacy_request(member_id, date_of_service, drug_name):
    """
    Orchestrates the pharmacy benefit verification process.

    Responsibilities:
    1. Receive the user's request (Goal)
    2. Build an execution plan
    3. Coordinate specialized agents
    4. Return one structured response
    """

    print("=" * 60)
    print("PharmaAssist AI - Orchestrator")
    print("=" * 60)

    # --------------------------------------------------
    # Goal
    # --------------------------------------------------
    print("\nGoal:")
    print(f"Determine whether Member {member_id} can receive '{drug_name}'.")

    # --------------------------------------------------
    # Execution Plan
    # --------------------------------------------------
    execution_plan = [
        "Eligibility Agent",
        "Coverage Agent",
        "Recommendation Agent",
        "Explanation Agent",
        "Evaluation Agent"
    ]

    print("\nExecution Plan:")
    for step in execution_plan:
        print(f"  → {step}")

    # --------------------------------------------------
    # Execute Eligibility Agent
    # --------------------------------------------------
    print("\nExecuting Eligibility Agent...")

    eligibility = check_eligibility(
        member_id=member_id,
        date_of_service=date_of_service
    )

    print(eligibility)

    if not eligibility["eligible"]:

        print("\nOrchestrator Decision:")
        print("Member is NOT eligible.")
        print("Stopping further agent execution.")

        return {
            "orchestrator_status": "STOPPED",
            "eligibility": eligibility
        }

    # --------------------------------------------------
    # Execute Coverage Agent
    # --------------------------------------------------
    print("\nExecuting Coverage Agent...")

    coverage = check_coverage(drug_name)

    print(coverage)

    # --------------------------------------------------
    # Execute Recommendation Agent
    # --------------------------------------------------
    print("\nExecuting Recommendation Agent...")

    recommendation = get_recommendation(
        eligible=eligibility["eligible"],
        covered=coverage["covered"],
        prior_authorization=coverage["prior_authorization"]
    )

    print(recommendation)

    # --------------------------------------------------
    # Execute Explanation Agent
    # --------------------------------------------------
    print("\nExecuting Explanation Agent...")

    explanation_data = {
        "eligible": eligibility["eligible"],
        "covered": coverage["covered"],
        "prior_authorization": coverage["prior_authorization"],
        "coverage_reason": coverage["coverage_reason"],
        "recommended_action": recommendation["recommended_action"]
    }

    explanation = explain_decision(explanation_data)

    print(explanation["explanation"])

    # --------------------------------------------------
    # Execute Evaluation Agent
    # --------------------------------------------------
    print("\nExecuting Evaluation Agent...")

    evaluation = evaluate_explanation(
        explanation_data,
        explanation["explanation"]
    )

    print(evaluation)

    # --------------------------------------------------
    # Final Orchestrated Response
    # --------------------------------------------------
    final_response = {
        "orchestrator_status": "SUCCESS",
        "goal": f"Determine coverage for {drug_name}",
        "execution_plan": execution_plan,
        "eligibility": eligibility,
        "coverage": coverage,
        "recommendation": recommendation,
        "explanation": explanation["explanation"],
        "evaluation": evaluation
    }

    return final_response


if __name__ == "__main__":

    result = process_pharmacy_request(
        member_id=1001,
        date_of_service="2026-05-01",
        drug_name="Ozempic"
    )

    print("\nFinal Orchestrator Response")
    print("=" * 60)
    print(result)