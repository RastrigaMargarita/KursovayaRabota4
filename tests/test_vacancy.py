import vacancy


def test_create():
    assert vacancy.Vacancy("123", "Заголовок", "http//www.ww.ru", "50", "100", "текст текст текст",
                           "текст текст текст", "Название компании").vacancy_id == "123"

    assert vacancy.Vacancy("123", "Заголовок", "http//www.ww.ru", "50", "100", "текст текст текст",
                           "текст текст текст", "Название компании").salary_min == 50

    assert vacancy.Vacancy("123", "Заголовок", "http//www.ww.ru", "sdfsad", "100", "текст текст текст",
                           "текст текст текст", "Название компании").salary_min == 0
