def get_recommendation(eligible, covered, prior_authorization):
    """
    Determines the next business action based on
    eligibility and coverage results.
    """

    # Rule 1
    if not eligible:
        return {
            "action_code": "CONTACT_BENEFITS",
            "recommended_action": "Contact Benefits Administrator"
        }

    # Rule 2
    if eligible and not covered:
        return {
            "action_code": "REVIEW_ALTERNATIVES",
            "recommended_action": "Review Covered Alternatives"
        }

    # Rule 3
    if eligible and covered and prior_authorization:
        return {
            "action_code": "SUBMIT_PA",
            "recommended_action": "Submit Prior Authorization"
        }

    # Rule 4
    return {
        "action_code": "FILL_PRESCRIPTION",
        "recommended_action": "Fill Prescription"
    }


if __name__ == "__main__":

    result = get_recommendation(
        eligible=False,
        covered=False,
        prior_authorization=False
    )

    print(result)