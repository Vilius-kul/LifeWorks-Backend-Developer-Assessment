import json

with open("assets/user.json") as f:
    data = json.load(f)
    print(data)
