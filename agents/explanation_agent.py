from ai.prompt_builder import build_explanation_prompt
from ai.gemini_client import generate_explanation


def explain_decision(explanation_data):
    """
    Generates a natural language explanation
    for the business decision.
    """

    prompt = build_explanation_prompt(explanation_data)

    explanation = generate_explanation(prompt)

    return {
        "status": "SUCCESS",
        "explanation": explanation
    }


if __name__ == "__main__":

    sample_data = {
        "eligible": True,
        "covered": True,
        "prior_authorization": True,
        "coverage_reason": "Covered with Prior Authorization",
        "recommended_action": "Submit Prior Authorization"
    }

    result = explain_decision(sample_data)

    print(result["explanation"])