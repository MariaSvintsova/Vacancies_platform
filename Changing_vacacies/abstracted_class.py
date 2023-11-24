from abc import ABC, abstractmethod


class Editoring_vacancies(ABC):

    @abstractmethod
    def delete_vacancy(self, vacancy_id):
        pass

    @abstractmethod
    def add_vacancy(self, data):
        pass

    @abstractmethod
    def get_vacancy_by_salary(self, salary):
        pass


