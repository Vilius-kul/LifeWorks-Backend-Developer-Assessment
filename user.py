from datetime import date, datetime


class User:
    def __init__(self, user_info) -> None:
        self.user_info = user_info

    def full_name(self):
        if "full_name" in self.user_info:
            pass
        else:
            self.user_info[
                "full_name"
            ] = f"{self.user_info['forename']} {self.user_info['surname']}"
        return self.user_info

    def age(self):
        b_day = datetime.strptime(
            self.user_info["date_of_birth"], "%Y/%m/%d"
        ).date()
        today = date.today()
        age = (
            today.year
            - b_day.year
            - ((today.month, today.day) < (b_day.month, b_day.day))
        )
        return age
