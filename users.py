from copy import deepcopy
from datetime import date, datetime
from typing import Dict, List


class Users:
    def __init__(self, users: List[Dict[str, str]]) -> None:
        self.users = deepcopy(users)

    def add_full_name(self) -> List[Dict[str, str]]:
        with_fullname: List[Dict[str, str]] = []
        for user in self.users:
            if "full_name" in user:
                with_fullname.append(user)
            else:
                updated_user = dict(list(user.items())[:2])
                updated_user[
                    "full_name"
                ] = f'{user.get("forename","")} {user.get("surname", "")}'
                updated_user.update(dict(list(user.items())[2:]))
                with_fullname.append(updated_user)

        return with_fullname

    def _age(self, user: Dict[str, str]) -> int:
        # data of birth string converted to datetime.date
        b_day = datetime.strptime(user["date_of_birth"], "%Y/%m/%d").date()
        today = date.today()

        # A bool that represents if today's day/month precedes the birth day/month
        one_or_zero = (today.month, today.day) < (b_day.month, b_day.day)
        year_difference = today.year - b_day.year
        age = year_difference - one_or_zero
        return age

    def thirty_and_over(self) -> List[Dict[str, str]]:
        thirty_and_over: List[Dict[str, str]] = []
        for user in self.users:
            if self._age(user) < 30:
                continue
            else:
                thirty_and_over.append(user)
        return thirty_and_over
