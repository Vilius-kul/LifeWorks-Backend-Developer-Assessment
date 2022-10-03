from typing import Dict, List

import pytest
from companies import Companies
from users import Users


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
            "date_of_birth": "2005/10/12",
            "location": "London",
            "company_id": 3,
        },
        {
            "surname": "Johnson",
            "date_of_birth": "2005/01/28",
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


@pytest.fixture
def dummy_companies() -> List[Dict[str, str]]:
    companies = [
        {
            "id": 1,
            "name": "Head Journal",
            "headquarters": "San Francisco",
            "industry": "Tech",
        },
        {
            "id": 2,
            "name": "Au Revoir Health",
            "headquarters": "Paris",
            "industry": "Health",
        },
        {
            "id": 3,
            "name": "Solomon Sisters Bank",
            "headquarters": "London",
            "industry": "Finance",
        },
    ]
    return companies


@pytest.fixture
def users_correct_data(dummy_users) -> Users:
    users_instance = Users(dummy_users)
    return users_instance


@pytest.fixture
def users_faulty_data(dummy_users_faulty_data) -> Users:
    users_instance = Users(dummy_users_faulty_data)
    return users_instance


@pytest.fixture
def companies_correct_data(dummy_users, dummy_companies) -> Companies:
    companies_instance = Companies(dummy_users, dummy_companies)
    return companies_instance
