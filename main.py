import json
from textwrap import indent

from pydantic import parse_obj_as

from company import Company
from user import User, age

with open("assets/company.json") as f:
    companies_info = json.load(f)

with open("assets/user.json") as f:
    users_info = json.load(f)

# #task1
# full_name = User.add_full_name(users_info)
# with open("task1.json", "w") as f:
#     json.dump(full_name, f, indent=4)

# task2
parsed_users = parse_obj_as(list[User], users_info)
for user in parsed_users:
    if age(user.date_of_birth) < 30:
        continue
    else:
        thirty_and_above = user.json()
    with open("task2.json", "a") as outfile:
        outfile.write(thirty_and_above)
