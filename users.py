from copy import deepcopy
from datetime import date, datetime


class Users:
    def __init__(self, users: list[dict[str, str]]) -> None:
        self.users = deepcopy(users)

    def add_full_name(self) -> list[dict]:
        with_fullname = []
        for user in self.users:
            if "full_name" in user:
                continue
            else:
                keys_list = list(user.keys())
                values_list = list(user.values())
                keys_list.insert(2, "full_name")
                values_list.insert(2, f"{values_list[0]} {values_list[1]}")
                with_fullname.append(dict(zip(keys_list, values_list)))

        return with_fullname

    def _age(self, user: dict) -> int:
        # data of birth string converted to datetime.date
        b_day = datetime.strptime(user["date_of_birth"], "%Y/%m/%d").date()
        today = date.today()

        # A bool that represents if today's day/month precedes the birth day/month
        one_or_zero = (today.month, today.day) < (b_day.month, b_day.day)
        year_difference = today.year - b_day.year
        age = year_difference - one_or_zero
        return age

    def thirty_and_over(self) -> list[dict[str, str]]:
        thirty_and_over = []
        for user in self.users:
            if self._age(user) < 30:
                continue
            else:
                thirty_and_over.append(user)
        return thirty_and_over
