from json_saver import JSONSaver
from source_api import HeadHunterAPI, SuperJobAPI
from vacancy import Vacancy
import config


def user_interaction():
    """Функция для взаимодействия с пользователем"""
    json_saver = JSONSaver()
    PLATFORMS = [HeadHunterAPI(config.HH_API_URL), SuperJobAPI(config.SJ_API_URL)]

    user_choise = ""
    while user_choise != '4':
        user_choise = input("""Введите действие: 
        0 - обновить вакансии с сайтов, 
        1 - добавить вакансию, 
        2 - удалить вакансию, 
        3 - посмотреть вакансии, 
        4 - прекратить работу
""")
        if user_choise == '0':
            key_word = input("Введите ключевое слово:")
            list_of_vacancies = []
            for PLATFORM in PLATFORMS:
                list_of_vacancies = list_of_vacancies + PLATFORM.get_vacancies(key_word, json_saver)
            json_saver.save_vacancies(list_of_vacancies)
            print(f"Загружено {len(list_of_vacancies)} вакансий")

        elif user_choise == '1':
            json_saver.add_vacancy(Vacancy(
                input("id вакансии: "),
                input("Заголовок: "),
                input("ссылка: "),
                input("минимум зарплаты: "),
                input("максимум зарплаты: "),
                input("требования: "),
                input("обязанности: "),
                input("название компании: ")))
            print("Вакансия добавлена")

        elif user_choise == '2':
            json_saver.delete_vacancy(
                input("id вакансии"))
            print("Вакансия удалена")
        elif user_choise == '3':
            user_choise_filter = input(
                "Отобрать по зарплате? 0- показать все, 1- указать зарплату, любой символ - отмена\n")
            if user_choise_filter == '0':
                json_saver.print_all_vacancies()
            elif user_choise_filter == '1':
                json_saver.get_vacancies_by_salary(int(input("Какая нужна зарплата?")))

        elif user_choise == '4':
            print("Пока, приходи еще.")


if __name__ == "__main__":
    user_interaction()
