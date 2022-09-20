from copy import deepcopy


class Companies:
    def __init__(
        self, users: list[dict[str, str]], companies: list[dict[str, str]]
    ) -> None:
        self.users = deepcopy(users)
        self.companies = deepcopy(companies)

    def _fetch_company(self, id, list_of_companies):
        for company in list_of_companies:
            if company["id"] == id:
                return company

    def add_company_field(self):
        with_company_filed = []
        for user in self.users:
            if "company" in user:
                continue
            else:
                user["company"] = self._fetch_company(
                    user["company_id"], self.companies
                )
                del user["company_id"]
                with_company_filed.append(user)
        return with_company_filed
