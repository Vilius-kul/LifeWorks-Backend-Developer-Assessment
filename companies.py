from copy import deepcopy
from typing import Any, Dict, List


class Companies:
    def __init__(
        self, users: List[Dict[str, Any]], companies: List[Dict[str, Any]]
    ) -> None:
        self.users = deepcopy(users)
        self.companies = deepcopy(companies)

    def _user_with_company_field(
        self, user: Dict[str, Any], companies: Dict[str, Dict[str, Any]]
    ) -> Dict[str, Any]:
        # new key with old key values, empty dict as a default value
        user["company"] = companies.get(f'{user.pop("company_id")}', {})
        return user

    def add_company_field(self) -> List[Dict[str, Any]]:
        with_company_filed: List[Dict[str, Any]] = []

        # new dict wit company id as a key
        companies = {f'{company["id"]}': company for company in self.companies}
        for user in self.users:
            with_company_filed.append(
                self._user_with_company_field(user, companies)
            )

        return with_company_filed
