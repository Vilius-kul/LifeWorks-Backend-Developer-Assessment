from datetime import date, datetime

from pydantic import BaseModel, validator


class User(BaseModel):
    forename: str
    surname: str
    date_of_birth: date
    location: str
    company_id: int

    @validator("date_of_birth", pre=True)
    def parse_birthdate(cls, value):
        return datetime.strptime(value, "%Y/%m/%d").date()

    @classmethod
    def add_full_name(cls, data: list[dict]):
        for user in data:
            if "full_name" in user:
                continue
            else:
                user["full_name"] = f"{user['forename']} {user['surname']}"
        return data


def age(dob: date):
    today = date.today()
    age = (
        today.year
        - dob.year
        - ((today.month, today.day) < (dob.month, dob.day))
    )
    return age


def thirty_and_above(data):
    for user in data:
        if age(user["date_of_birth"]) < 30:
            continue
        else:
            print(user)
