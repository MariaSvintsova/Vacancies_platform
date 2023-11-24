import os
from pprint import pprint

from dotenv import load_dotenv

from Classes_for_API.abstracted_class import For_apies
import json
import requests

from Classes_for_API.implemented import api_key


class SuperJobAPI(For_apies):

    url = "https://api.superjob.ru/2.0"

    def __init__(self, filter_words):
        self.filter_words = filter_words
        self.params = {
            "keyword" : self.filter_words
        }



    def get_vacancies(self):

        all_vacancies = []
        headers = {
            "Host": "api.superjob.ru",
            "X-Api-App-Id": api_key,
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = requests.get(f"{self.url}/vacancies", headers=headers, params=self.params).json()


        for vacancy in data["objects"]:

            if vacancy.get("address") is not None:
                city = vacancy.get("address").split(',')[0]
            else:
                city = "Не указано"


            new_vacancy = {
                "id": vacancy.get("id"),
                "name" : vacancy.get("profession", "Не указано"),
                "salary_to" : vacancy.get("payment_to", "не указано"),
                "salary_from" : vacancy.get("payment_from", "не указано"),
                "description" : vacancy.get("candidat", "Не указано"),
                "city" : city,
                "platform" : "SuperJob"
            }

            all_vacancies.append(new_vacancy)


        return all_vacancies
#
# ggg = SuperJobAPI("Продавец")
# print(ggg.get_vacancies())


