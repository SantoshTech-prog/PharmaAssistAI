import csv
from pathlib import Path


def check_coverage(drug_name):
    """
    Checks whether the requested drug is covered
    and whether Prior Authorization is required.
    """

    base_dir = Path(__file__).resolve().parent.parent
    data_file = base_dir / "data" / "drugs.csv"

    with open(data_file, mode="r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["DrugName"].strip().lower() == drug_name.strip().lower():

                covered = row["Covered"].strip().lower() == "yes"
                pa_required = row["PriorAuthorization"].strip().lower() == "yes"

                if covered:
                    if pa_required:
                        reason = "Covered with Prior Authorization"
                    else:
                        reason = "Covered"
                else:
                    reason = "Drug is not covered under the benefit plan"

                return {
                    "drug_name": row["DrugName"],
                    "drug_number": row["DrugNumber"],
                    "covered": covered,
                    "prior_authorization": pa_required,
                    "coverage_reason": reason
                }

    return {
        "drug_name": drug_name,
        "covered": False,
        "prior_authorization": False,
        "coverage_reason": "Drug not found"
    }


if __name__ == "__main__":

    result = check_coverage("Ozempic")

    print(result)