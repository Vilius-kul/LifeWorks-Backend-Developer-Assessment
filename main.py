import json

with open("assets/user.json") as f:
    data = json.load(f)

for user in data:
    if "full_name" in user:
        continue
    else:
        user["full_name"] = f"{user['forename']} {user['surname']}"

print(data)
