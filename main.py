import json

from user import User

with open("assets/company.json") as f:
    companies_info = json.load(f)

with open("assets/user.json") as f:
    users_data = json.load(f)

# task_1
def add_full_name(users_info):
    with_full_name = []
    for user in users_info:
        with_full_name.append(User(user).full_name())
    return with_full_name


# task_2
def thirty_and_over(users_info):
    thirty_and_over = []
    for user in users_info:
        if User(user).age() < 30:
            continue
        else:
            thirty_and_over.append(user)
    return thirty_and_over
