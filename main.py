import json

from company import Company
from user import User

with open("assets/company.json") as f:
    companies_info = json.load(f)

with open("assets/user.json") as f:
    users_info = json.load(f)


for user in users_info:
    print(User(**user))
