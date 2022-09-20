import json

from companies import Companies
from users import Users

with open("assets/company.json") as f:
    companies_data = json.load(f)

with open("assets/user.json") as f:
    users_data = json.load(f)


answers_path = "answers/"

users_info = Users(users_data)

# task_1
users_with_fullname = users_info.add_full_name()
with open(f"{answers_path}task_one.json", "w") as outfile:
    json.dump(users_with_fullname, outfile)


# task_2
users_older_than_30 = users_info.thirty_and_over()
with open(f"{answers_path}task_two.json", "w") as outfile:
    json.dump(users_older_than_30, outfile)


# task_3
companies_info = Companies(users_data, companies_data)
with_company_field = companies_info.add_company_field()
with open(f"{answers_path}task_three.json", "w") as outfile:
    json.dump(with_company_field, outfile)
