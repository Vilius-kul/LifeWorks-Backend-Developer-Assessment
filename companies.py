from copy import deepcopy
from typing import Dict, List


class Companies:
    def __init__(
        self, users: List[Dict[str, str]], companies: List[Dict[str, str]]
    ) -> None:
        self.users = deepcopy(users)
        self.companies = deepcopy(companies)

    def _user_with_company_field(self, user: Dict, companies: Dict[str, Dict]):
        user["company"] = companies.get(f'{user.pop("company_id")}', {})
        return user

    def add_company_field(self):
        with_company_filed: List[Dict[str, str]] = []
        # new dict wit company id as a key
        companies = {f'{company["id"]}': company for company in self.companies}
        for user in self.users:
            with_company_filed.append(
                self._user_with_company_field(user, companies)
            )
        return with_company_filed
