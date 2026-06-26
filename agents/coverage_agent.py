import csv
from pathlib import Path


def check_coverage(drug_name):

    base_dir = Path(__file__).resolve().parent.parent
    data_file = base_dir / "data" / "drugs.csv"

    with open(data_file, mode="r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["DrugName"].lower() == drug_name.lower():

                covered = row["Covered"]
                pa_required = row["PriorAuthorization"]

                if covered == "Yes":
                    if pa_required == "Yes":
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
        "covered": "No",
        "prior_authorization": "No",
        "coverage_reason": "Drug not found"
    }


if __name__ == "__main__":
    result = check_coverage("Ozempic")
    print(result)