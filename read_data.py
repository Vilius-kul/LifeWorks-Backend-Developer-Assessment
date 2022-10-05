import json
from typing import Any, Dict, List


class DataReader:
    def __init__(self, users_path: str, companies_path: str) -> None:
        self.users_path = users_path
        self.companies_path = companies_path

    def read_companies(self) -> List[Dict[str, Any]]:
        # "assets/company.json"
        with open(self.companies_path) as f:
            companies_data = json.load(f)
        return companies_data

    def read_users(self) -> List[Dict[str, Any]]:
        # "assets/user.json"
        with open(self.users_path) as f:
            users_data = json.load(f)
        return users_data
