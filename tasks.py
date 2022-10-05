import json

from companies import Companies
from users import Users


class Tasks:
    def __init__(
        self, users_info: Users, companies_info: Companies, answers_path: str
    ) -> None:
        self.users_info = users_info
        self.companies_info = companies_info
        self.answers_path = answers_path

    # task_1
    def task_1(self) -> None:
        users_with_fullname = self.users_info.add_full_name()
        with open(f"{self.answers_path}task_one.json", "w") as outfile:
            json.dump(users_with_fullname, outfile, indent=4)

    # # task_2
    def task_2(self) -> None:
        users_older_than_30 = self.users_info.thirty_and_over()
        with open(f"{self.answers_path}task_two.json", "w") as outfile:
            json.dump(users_older_than_30, outfile, indent=4)

    # task_3
    def task_3(self) -> None:
        with_company_field = self.companies_info.add_company_field()
        with open(f"{self.answers_path}task_three.json", "w") as outfile:
            json.dump(with_company_field, outfile, indent=4)
