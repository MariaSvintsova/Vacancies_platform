import json
from Classes_for_API.abstracted_class import For_apies
import requests


class HeadHunterAPI(For_apies):

    def __init__(self, text):
        self.text = text



    def get_vacancies(self):

        url = "https://api.hh.ru"
        params = {
            'text': self.text,
            'only_with_salary': 'true'
        }

        all_vacancies = []
        data = requests.get(f"{url}/vacancies", params=params).json()
        # pretty_data = json.dumps(data, indent=4)
        for vacancy in data['items']:

            address = vacancy.get('address', {})
            if address is not None:
                city = address.get("city")
            else:
                city = "Не указано"

            salary = vacancy.get("salary", {})
            if salary is not None:
                salary_to = salary.get("to")
            else:
                salary_to ="Не указано"

            salary = vacancy.get("salary", {})
            if salary is not None:
                salary_from = salary.get("from")
            else:
                salary_from = "Не указано"

            new_vacancy = {
            'id' : vacancy.get("id", "Не указано"),
            "name" : vacancy.get("name", "Не указано"),
            "requirements" : vacancy.get("snippet", {}).get("requirement"),
            "description" : vacancy.get("description", "Не указано"),
            "salary_to" : salary_to,
            "salary_from" : salary_from,
            "city" : city,
            "platform" : "HeadHunter"
            }

            all_vacancies.append(new_vacancy)



        return all_vacancies

# uhfhf = HeadHunterAPI()
# print(uhfhf.get_vacancies())










