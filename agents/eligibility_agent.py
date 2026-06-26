import csv
from datetime import datetime
from pathlib import Path


def check_eligibility(member_id, date_of_service):
    base_dir = Path(__file__).resolve().parent.parent
    data_file = base_dir / "data" / "members.csv"

    with open(data_file, mode="r") as file:
        reader = csv.DictReader(file)

        for row in reader:

            if row["MemberID"] == str(member_id):

                start_date = datetime.strptime(
                    row["EligibilityStart"],
                    "%Y-%m-%d"
                )

                end_date = datetime.strptime(
                    row["EligibilityEnd"],
                    "%Y-%m-%d"
                )

                service_date = datetime.strptime(
                    date_of_service,
                    "%Y-%m-%d"
                )

                if start_date <= service_date <= end_date:

                    return {
                        "eligible": True,
                        "member_id": member_id,
                        "message": "Member is eligible"
                    }

                else:

                    return {
                        "eligible": False,
                        "member_id": member_id,
                        "message": "Member is not eligible"
                    }

        return {
            "eligible": False,
            "member_id": member_id,
            "message": "Member not found"
        }
if __name__ == "__main__":
    result = check_eligibility(
        member_id=1001,
        date_of_service="2026-05-01"
    )
    print(result)