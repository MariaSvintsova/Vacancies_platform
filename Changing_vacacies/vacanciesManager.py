import json
from Changing_vacacies.abstracted_class import Editoring_vacancies

class JsonFileManager(Editoring_vacancies):

    def __init__(self, file_path):
        self.file_path = file_path

    def _get_all_vacancies(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                # file_content = file.read()
                # return json.loads(file_content)
                return json.load(file)
        except FileNotFoundError as e:
            print(f"Error reading the file: {e}")
            return []
        except Exception as e:
            print(f"Error reading the file: {e}")
            return []

    def _save_vacancies(self, jobs):
        with open(self.file_path, "w", encoding="utf-8") as filee:
            json.dump(jobs, filee, indent=2)


    def add_vacancy(self, data):
        all_vacancies = self._get_all_vacancies()
        all_vacancies.append(data)
        self._save_vacancies(all_vacancies)

    def get_vacancy_by_salary(self, salary):
        all_vacancies = self._get_all_vacancies()
        good_vacancies = []
        for vacancy in all_vacancies:
            if vacancy.get("salary_to") is not None:
                if vacancy.get("salary_to", 0) >= salary:
                    good_vacancies.append(vacancy)
            else:
                if vacancy.get("salary_from", 0) >= salary:
                    good_vacancies.append(vacancy)
        # good_vacancies = [vacancy for vacancy in all_vacancies if vacancy.get('salary_to', 0) >= salary or vacancy.get("salary_from", 0) >= salary]
        return good_vacancies

    def delete_vacancy(self, vacancy_id):
        all_vacancies = self._get_all_vacancies()
        updated_vacancies = [vacancy for vacancy in all_vacancies if vacancy.get("id") != vacancy_id]
        self._save_vacancies(updated_vacancies)

    # for main function
    def get_vacancy_by_id(self, vacancy_id):
        all_vacancies = self._get_all_vacancies()
        for vacancy in all_vacancies:
            if vacancy.get("id") == f"{vacancy_id}":
                return vacancy




file_manager = JsonFileManager("/Users/miya/PycharmProjects/Vacancies_platform/Changing_vacacies/vacancies.json")

# adding_vacancy
# vacancy1 = {"id" : 1, "title" : "developer", "link" : "link", "short_description": "тру-ла-ла", "salary_to" : 90000}
# vacancy2 = {"id" : 2, "title" : "developer", "link" : "link", "short_description": "тру-ла-ла", "salary_to" : 60000}
# vacancy3 = {"id" : 3, "title" : "developer", "link" : "link", "short_description": "тру-ла-ла", "salary_to" : 30000}

# file_manager.add_vacancy(vacancy1)
# file_manager.add_vacancy(vacancy2)
# file_manager.add_vacancy(vacancy3)

# print(file_manager.get_vacancy_by_id(89313067))

# print(file_manager.get_vacancy_by_salary(60000))

# file_manager.delete_vacancy(2)







