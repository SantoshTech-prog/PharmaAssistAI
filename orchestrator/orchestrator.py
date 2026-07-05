from agents.evaluation_agent import evaluate_explanation
from agents.explanation_agent import explain_decision
from agents.eligibility_agent import check_eligibility
from agents.coverage_agent import check_coverage
from agents.recommendation_agent import get_recommendation


def process_pharmacy_request(member_id, date_of_service, drug_name, verbose=False):
    """
    Orchestrates the pharmacy benefit verification process.

    Responsibilities:
    1. Receive the user's request (Goal)
    2. Build an execution plan
    3. Coordinate specialized agents
    4. Return one structured response
    """

    if verbose:
        print("=" * 60)
        print("PharmaAssist AI - Orchestrator")
        print("=" * 60)

    # --------------------------------------------------
    # Goal
    # --------------------------------------------------
    if verbose:
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

    if verbose:
        print("\nExecution Plan:")
        for step in execution_plan:
            print(f"  → {step}")

    # --------------------------------------------------
    # Execute Eligibility Agent
    # --------------------------------------------------
    if verbose:
        print("\nExecuting Eligibility Agent...")

    eligibility = check_eligibility(
        member_id=member_id,
        date_of_service=date_of_service
    )

    if verbose:
        print(eligibility)

    if not eligibility["eligible"]:

        if verbose:
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
    if verbose:
        print("\nExecuting Coverage Agent...")

    coverage = check_coverage(drug_name)

    if verbose:
        print(coverage)

    # --------------------------------------------------
    # Execute Recommendation Agent
    # --------------------------------------------------
    if verbose:
        print("\nExecuting Recommendation Agent...")

    recommendation = get_recommendation(
        eligible=eligibility["eligible"],
        covered=coverage["covered"],
        prior_authorization=coverage["prior_authorization"]
    )

    if verbose:
        print(recommendation)

    # --------------------------------------------------
    # Execute Explanation Agent
    # --------------------------------------------------
    if verbose:
        print("\nExecuting Explanation Agent...")

    explanation_data = {
        "eligible": eligibility["eligible"],
        "covered": coverage["covered"],
        "prior_authorization": coverage["prior_authorization"],
        "coverage_reason": coverage["coverage_reason"],
        "recommended_action": recommendation["recommended_action"]
    }

    explanation = explain_decision(explanation_data)

    if verbose:
        print(explanation["explanation"])

    # --------------------------------------------------
    # Execute Evaluation Agent
    # --------------------------------------------------
    if verbose:
        print("\nExecuting Evaluation Agent...")

    evaluation = evaluate_explanation(
        explanation_data,
        explanation["explanation"]
    )

    if verbose:
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
        drug_name="Ozempic",
        verbose=True
    )

    print("\nFinal Orchestrator Response")
    print("=" * 60)
    print(result)