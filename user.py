import json
from datetime import date, datetime

from pydantic import BaseModel, validator

with open("assets/user.json") as f:
    data = json.load(f)


class User(BaseModel):
    forename: str
    surname: str
    date_of_birth: date
    location: str
    company_id: int

    @validator("date_of_birth", pre=True)
    def parse_birthdate(cls, value):
        return datetime.strptime(value, "%Y/%m/%d").date()
