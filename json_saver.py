import json

from vacancy import Vacancy


class JSONSaver:
    """Класс для хранения полученных вакансиях
    Позволяет добавлять: add_vacancy
              удалять: delete_vacancy
              """
    FILE_NAME = "data.json"

    def __init__(self):
        self.local_list = []
        with open(self.FILE_NAME, "r") as f:
            try:
                json_data = json.loads(f.read())
                for x in json_data:
                    self.local_list.append(Vacancy(x['vacancy_id'],
                                                   x['title'],
                                                   x['ref'],
                                                   x['salary_min'],
                                                   x['salary_max'],
                                                   x['requirements'],
                                                   x['responsibility'],
                                                   x['employer']))
            except Exception:
                print("Кажется у нас нет еще ни одной сохраненной вакансии, начнем с нуля")

    def add_vacancy(self, vacancy):
        self.local_list.append(vacancy)
        self.save_vacancies()

    def get_vacancies_by_salary(self, param):

        list_to_return = []

        for x in self.local_list:
            if x.salary_min is not None:
                if param < x.salary_min:
                    continue
            if x.salary_max is not None:
                if x.salary_max < param:
                    continue
            list_to_return.append(x)
        [print(x.__dict__) for x in list_to_return]

    def delete_vacancy(self, v_id):
        self.save_vacancies([x for x in self.local_list if x.vacancy_id != v_id])

    def save_vacancies(self, list_of_vacancies=None):
        if list_of_vacancies is not None:
            self.local_list = list_of_vacancies
        with open(self.FILE_NAME, "w") as f:
            json.dump([x.__dict__ for x in self.local_list], f)

    def print_all_vacancies(self):
        [print(x.__dict__) for x in self.local_list]
