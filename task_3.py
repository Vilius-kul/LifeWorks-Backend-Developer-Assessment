import json

with open("assets/company.json") as f:
    data = json.load(f)

with open("assets/user.json") as f:
    user_info = json.load(f)


def fetch_company_data(user):
    company_id = user["company_id"]
    for company_info in companies_data:
        if company_info["id"] == company_id:
            return company_info


def task_3(data, user):
    for user in data:
        if "company" in user:
            continue
        else:
            user["company"] = fetch_company_data(user)
