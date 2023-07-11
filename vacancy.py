class Vacancy:
    """Класс для данных о вакансии
        :param v_id: string
        :param v_name: string
        :param v_url: string
        :param s_from: int
        :param s_to: int
        :param v_requirement: string
        :param v_responsibility: string
        :param c_name: string

    """

    def __init__(self, v_id=None, v_name=None, v_url=None, s_from=None, s_to=None, v_requirement=None,
                 v_responsibility=None, c_name=None):

        self.vacancy_id = str(v_id)
        self.title = v_name
        self.ref = v_url
        try:
            self.salary_min = int(s_from)
        except Exception:
            self.salary_min = 0
        try:
            self.salary_max = int(s_to)
        except Exception:
            self.salary_max = 0
        self.requirements = v_requirement
        self.responsibility = v_responsibility
        self.employer = c_name

    def __lt__(self, other):
        return self.salary_max < other.salary_max
