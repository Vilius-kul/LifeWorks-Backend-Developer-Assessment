import json

with open("assets/company.json") as f:
    companies_data = json.load(f)


def task_3(data):
    for user in data:
        if "company" in user:
            continue
        else:
            user["company"] = {}


def fetch_company_data(user):
    company_id = user["company_id"]
    for company in companies_data:
        if company["id"] == company_id:
            print(company)


for company in companies_data:
    if company["id"] == 2:
        print(company)
