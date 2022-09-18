from datetime import date

from user import User


class Transformer:
    def add_full_name(self, data: list[dict]):
        for user in data:
            if "full_name" in user:
                continue
            else:
                user["full_name"] = f"{user['forename']} {user['surname']}"
        return data

    @staticmethod
    def age(dob: date):
        today = date.today()
        age = (
            today.year
            - dob.year
            - ((today.month, today.day) < (dob.month, dob.day))
        )
        return age

    @classmethod
    def thirty_and_above(cls, users_info):
        filtered_users = []
        for user in users_info:
            parsed_user_info = User(**user)
            if age(parsed_user_info.date_of_birth) < 30:
                continue
            else:
                filtered_users.append(user)
        return filtered_users
