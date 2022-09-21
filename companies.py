from copy import deepcopy


class Companies:
    def __init__(self, users, companies):
        self.users = deepcopy(users)
        self.companies = deepcopy(companies)

    def _user_with_company_field(self, user, company):
        for k, v in company.items():
            if user["company_id"] == int(k):
                user["company_id"] = v
        # rename key
        user["company"] = user.pop("company_id")
        return user

    def add_company_field(self):
        with_company_filed = []
        # new dict wit company id as a key
        companies = {f'{company["id"]}': company for company in self.companies}
        for user in self.users:
            with_company_filed.append(
                self._user_with_company_field(user, companies)
            )
        return with_company_filed
