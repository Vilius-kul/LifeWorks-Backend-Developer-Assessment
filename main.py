import json

from companies import Companies
from users import Users

with open("assets/company.json") as f:
    companies_data = json.load(f)

with open("assets/user.json") as f:
    users_data = json.load(f)


# task_1
print("-" * 50 + "task_1" + "-" + "-" * 50)
print()
users_info = Users(users_data)
print(users_info.add_full_name())
print()
print("-" * 50 + "task_2" + "-" + "-" * 50)
print()

# task_2
print(users_info.thirty_and_over())
print()
print("-" * 50 + "task_3" + "-" + "-" * 50)
print()

# task_3
companies_info = Companies(users_data, companies_data)
print(companies_info.add_company_field())
