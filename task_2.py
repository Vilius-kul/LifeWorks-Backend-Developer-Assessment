import json
from datetime import date, datetime

from user import User

with open("assets/user.json") as f:
    users_info = json.load(f)


def age(dob):
    # b_day = datetime.strptime(dob, "%Y/%m/%d").date()
    today = date.today()
    age = (
        today.year
        - dob.year
        - ((today.month, today.day) < (dob.month, dob.day))
    )
    return age


def thirty_and_above(user_data):
    for user in user_data:
        if age(user["date_of_birth"]) < 30:
            continue
        else:
            print(user)


test_dob = "1987/08/15"

user1 = User(**users_info[0])


print(age(user1.date_of_birth))
