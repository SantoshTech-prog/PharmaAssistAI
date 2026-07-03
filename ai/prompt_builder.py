def build_explanation_prompt(explanation_data):
    """
    Builds a prompt for Gemini using only the
    minimum information required for explanation.
    """

    eligible = explanation_data["eligible"]
    covered = explanation_data["covered"]
    prior_auth = explanation_data["prior_authorization"]
    coverage_reason = explanation_data["coverage_reason"]
    recommended_action = explanation_data["recommended_action"]

    prompt = f"""
You are an expert Pharmacy Benefits Assistant.

Your job is to explain the pharmacy benefit decision to a member in clear,
simple, and professional language.

Do NOT change the business decision.

Only explain it.

Business Decision:

Member Eligible: {eligible}

Drug Covered: {covered}

Prior Authorization Required: {prior_auth}

Coverage Reason:
{coverage_reason}

Recommended Action:
{recommended_action}

Generate a friendly explanation in less than 150 words.
"""

    return prompt


if __name__ == "__main__":

    sample_data = {
        "eligible": True,
        "covered": True,
        "prior_authorization": True,
        "coverage_reason": "Covered with Prior Authorization",
        "recommended_action": "Submit Prior Authorization"
    }

    print(build_explanation_prompt(sample_data))