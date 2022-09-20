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
        b_day = datetime.strptime(user["date_of_birth"], "%Y/%m/%d").date()
        today = date.today()
        age = (
            today.year
            - b_day.year
            - ((today.month, today.day) < (b_day.month, b_day.day))
        )
        return age

    def thirty_and_over(self) -> list[dict[str, str]]:
        thirty_and_over = []
        for user in self.users:
            if self._age(user) < 30:
                continue
            else:
                thirty_and_over.append(user)
        return thirty_and_over
