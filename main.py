import json
from pprint import pprint

from Changing_vacacies.vacanciesManager import JsonFileManager
from Classes_for_API.HeadHunterAPI import HeadHunterAPI
from Classes_for_API.SuperJobAPI import SuperJobAPI
from HandleJob import Handle_job


def conversation_with_user():
    platform = int(input("Добрый день! Какую платформу для выбора вакансий вы предпочитаете?\n1 - HeadHunter, 2 - SuperJob: "))
    if platform == 1:
        print("Welcome to HeadHunter vacancies!")
    elif platform == 2:
        print("Welcome to SuperJob vacancies!")
    profession = input("Вакансии по каким профессиям вы бы хотели рассмотреть? ")

    manager = JsonFileManager('Changing_vacacies/vacancies.json')

    if platform == 1:
        list_of_jobs = HeadHunterAPI(profession)
        final_list = list_of_jobs.get_vacancies()
        for job in final_list:
            manager.add_vacancy(job)
    elif platform == 2:
        list_of_jobs = SuperJobAPI(profession)
        final_list = list_of_jobs.get_vacancies()
        for job in final_list:
            manager.add_vacancy(job)




    wanted_salary = int(input("ВВедите желаемую зарплату и будет выведен список подходящих вам вакансий: "))

    pprint(manager.get_vacancy_by_salary(wanted_salary))

    chosen_action = int(input("Выберите следующее действие:\n"
                              "1: Хочу добавить вакансию в список\n"
                              "2: Хочу удалить вакансию по id\n"
                              "3: Хочу сравнить по зарплате две вакансии "))
    if chosen_action == 1:
        data_newvacancy = input("Введите данные новой вакансии: ")

        manager.add_vacancy(json.loads(data_newvacancy))
        # print(json.dump(data_newvacancy))
        print("\nВакансия добавлена")
    elif chosen_action == 2:
        id_deletingvacancy = input("Id вакансии, которую надо удалить: ")
        manager.delete_vacancy(id_deletingvacancy)
        print(f"Вакансия с id {id_deletingvacancy} удалена")
    elif chosen_action == 3:
        job1 = int(input("Сравнение двух вакансий, введите id первой: "))
        job2 = int(input("Введите id второй: "))

        ex1 = manager.get_vacancy_by_id(f"{job1}")
        ex2 = manager.get_vacancy_by_id(f"{job2}")


        self_job = Handle_job(ex1.get('name'), ex1.get("city"), ex1.get("salary_to"), ex1.get("salary_from"), ex1.get('description'))
        other_job = Handle_job(ex2.get('name'), ex2.get("city"), ex2.get("salary_to"), ex2.get("salary_from"), ex2.get('description'))

        if self_job > other_job:
            print("Вакансия 1 имеет большую зарплату")
        elif self_job == other_job:
            print("Вакансия 1 и 2 имеет одинаковые зарплаты")
        elif self_job < other_job:
            print("Вакансия 1 имеет меньшую зарплату")




if __name__ == "__main__":
    conversation_with_user()
