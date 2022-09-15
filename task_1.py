def full_name(data):
    for user in data:
        if "full_name" in user:
            continue
        else:
            user["full_name"] = f"{user['forename']} {user['surname']}"

    print(data)
