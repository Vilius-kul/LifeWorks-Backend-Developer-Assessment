from companies import Companies
from read_data import DataReader
from tasks import Tasks
from users import Users


def main():

    path_to_companies = "assets/company.json"
    path_to_users = "assets/user.json"
    answers_path = "answers/"

    data = DataReader(path_to_users, path_to_companies)

    users_data = data.read_users()
    companies_data = data.read_companies()

    companies_info = Companies(users_data, companies_data)
    users_info = Users(users_data)

    tasks_instance = Tasks(users_info, companies_info, answers_path)

    tasks_instance.task_1()
    tasks_instance.task_2()
    tasks_instance.task_3()


if __name__ == "__main__":
    main()
