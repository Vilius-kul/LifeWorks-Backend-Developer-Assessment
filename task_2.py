from datetime import date, datetime


def age(dob):
    b_day = datetime.strptime(dob, "%Y/%m/%d").date()
    today = date.today()
    age = (
        today.year
        - b_day.year
        - ((today.month, today.day) < (b_day.month, b_day.day))
    )
    return age


def thirty_and_above(data):
    for user in data:
        if age(user["date_of_birth"]) < 30:
            continue
        else:
            print(user)


test_dob = "1987/08/15"


age(test_dob)
