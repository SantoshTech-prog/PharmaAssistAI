def evaluate_explanation(decision, explanation):
    """
    Evaluates whether the AI-generated explanation
    is consistent with the structured business decision.
    """

    issues = []
    score = 100

    explanation_lower = explanation.lower()

    # ----------------------------------------
    # Rule 1 - Coverage
    # ----------------------------------------
    if decision["covered"]:
        if "not covered" in explanation_lower:
            issues.append(
                "Explanation incorrectly states that the drug is not covered."
            )
            score -= 30

    # ----------------------------------------
    # Rule 2 - Prior Authorization
    # ----------------------------------------
    if decision["prior_authorization"]:
        if "prior authorization" not in explanation_lower:
            issues.append(
                "Prior Authorization requirement was not mentioned."
            )
            score -= 25

    # ----------------------------------------
    # Rule 3 - Recommended Action
    # ----------------------------------------
    if "submit prior authorization" in decision["recommended_action"].lower():
        if (
            "submit" not in explanation_lower
            and "doctor" not in explanation_lower
        ):
            issues.append(
                "Recommended action is missing from the explanation."
            )
            score -= 20

    # ----------------------------------------
    # Rule 4 - Empty Explanation
    # ----------------------------------------
    if len(explanation.strip()) == 0:
        issues.append("Explanation is empty.")
        score = 0

    passed = len(issues) == 0

    summary = (
        "Explanation is consistent with the structured business decision."
        if passed
        else "Explanation needs improvement."
    )

    return {
        "passed": passed,
        "score": score,
        "issues": issues,
        "summary": summary
    }


if __name__ == "__main__":

    decision = {
        "covered": True,
        "prior_authorization": True,
        "recommended_action": "Submit Prior Authorization"
    }

    explanation = """
    Your medication is covered under your plan.
    However, Prior Authorization is required.
    Please ask your doctor to submit the request.
    """

    result = evaluate_explanation(decision, explanation)

    print(result)