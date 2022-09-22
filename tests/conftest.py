from typing import Dict, List

import pytest


@pytest.fixture
def dummy_users() -> List[Dict[str, str]]:
    users = [
        {
            "forename": "Jane",
            "surname": "Smith",
            "date_of_birth": "2001/10/12",
            "location": "London",
            "company_id": 3,
        },
        {
            "forename": "Mark",
            "surname": "Johnson",
            "date_of_birth": "1987/01/28",
            "location": "New York",
            "company_id": 1,
        },
    ]
    return users


@pytest.fixture
def dummy_users_faulty_data() -> List[Dict[str, str]]:
    users = [
        {
            "forename": "Jane",
            "date_of_birth": "2001/10/12",
            "location": "London",
            "company_id": 3,
        },
        {
            "surname": "Johnson",
            "date_of_birth": "1987/01/28",
            "location": "New York",
            "company_id": 1,
        },
        {
            "forename": "Jane",
            "surname": "Doe",
            "full_name": "Jane Doe",
            "date_of_birth": "2005/10/12",
            "location": "London",
            "company_id": 2,
        },
        {
            "date_of_birth": "2005/10/12",
            "location": "London",
            "company_id": 2,
        },
    ]
    return users
