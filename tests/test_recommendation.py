from agents.eligibility_agent import check_eligibility
from agents.coverage_agent import check_coverage


def run_workflow(member_id, service_date, drug_name):

    print("=" * 50)
    print("PharmaAssist AI Workflow Started")
    print("=" * 50)

    # Step 1 - Eligibility
    eligibility = check_eligibility(member_id, service_date)

    print("\nEligibility Result")
    print(eligibility)

    if not eligibility["eligible"]:
        print("\nWorkflow Stopped")
        print("Reason:", eligibility["message"])
        return

    # Step 2 - Coverage
    coverage = check_coverage(drug_name)

    print("\nCoverage Result")
    print(coverage)

    print("\nWorkflow Complete")


run_workflow(
    member_id=1001,
    service_date="2026-05-01",
    drug_name="Ozempic"
)