from datetime import date, datetime


class Users:
    def __init__(self, users) -> None:
        self.users = users

    def add_full_name(self):
        with_fullname = []
        for user in self.users:
            if "full_name" in user:
                continue
            else:
                user["full_name"] = f"{user['forename']} {user['surname']}"
                with_fullname.append(user)
        return with_fullname

    def _age(self, user):
        b_day = datetime.strptime(user["date_of_birth"], "%Y/%m/%d").date()
        today = date.today()
        age = (
            today.year
            - b_day.year
            - ((today.month, today.day) < (b_day.month, b_day.day))
        )
        return age

    def thirty_and_over(self):
        thirty_and_over = []
        for user in self.users:
            if self._age(user) < 30:
                continue
            else:
                thirty_and_over.append(user)
        return thirty_and_over
