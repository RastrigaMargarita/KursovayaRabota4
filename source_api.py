from abc import ABC, abstractmethod
import requests

from vacancy import Vacancy


class SourceAPI(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self, keyword, json_saver):
        pass


class HeadHunterAPI(SourceAPI):
    """Класс для загрузки вакансий с hh.ru"""

    def __init__(self, ):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'School task(rastrm@mail.ru)'}

    def get_vacancies(self, keyword, json_saver):
        """Функция загружает вакансии с сайта HeadHunter по ключевому слову
        :param keyword: string
        :param json_saver: JSONSever object"""

        param = {'text': keyword, 'archived': 'False'}
        response = requests.get(self.url, headers=self.headers, params=param)

        if response.status_code != 200:
            raise Exception("Не могу получить вакансии")
        else:
            list_of_vacancies = []
            for vacancy_item in response.json()["items"]:
                list_of_vacancies.append(Vacancy(vacancy_item['id'], vacancy_item['name'], vacancy_item['url'],
                                                 (vacancy_item['salary']['from'] if vacancy_item[
                                                                                    'salary'] is not None else None),
                                                 (vacancy_item['salary']['to'] if vacancy_item[
                                                                                    'salary'] is not None else None),
                                                 vacancy_item['snippet']['requirement'],
                                                 vacancy_item['snippet']['responsibility'],
                                                 vacancy_item['employer']['name']))

            return list_of_vacancies


class SuperJobAPI(SourceAPI):
    """Класс для загрузки вакансий с rabota.ru"""

    def __init__(self, ):
        self.url = 'https://api.superjob.ru/2.0/vacancies/'
        self.headers = {
            'X-Api-App-Id':
                'v3.r.13770101.c42aca0a79d66f7e7c83ca940cca366b0f08f7e3.4dfeb86a210ff0e5cce5e3de633886a8de559f61'}

    def get_vacancies(self, keyword, json_saver):
        """Функция загружает вакансии с сайта HeadHunter по ключевому слову
        :param keyword: string
        :param json_saver: JSONSaver object """

        param = {'keyword': keyword, 'archived': 'False', 'count': 30}
        response = requests.get(self.url, headers=self.headers, params=param)

        if response.status_code != 200:
            raise Exception("Не могу получить вакансии")
        else:
            list_of_vacancies = []
            for vacancy_item in response.json()["objects"]:
                list_of_vacancies.append(Vacancy(vacancy_item['id'], vacancy_item['profession'], vacancy_item['link'],
                                                 vacancy_item['payment_from'],
                                                 vacancy_item['payment_to'],
                                                 vacancy_item['candidat'],
                                                 None,
                                                 vacancy_item['firm_name']))

            return list_of_vacancies
