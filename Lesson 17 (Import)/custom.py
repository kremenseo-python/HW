from .employee import Employee
"""Импортируем класс сотрудников"""
from .exception import UnableToWorkException
"""Импортируем ..."""


class Programmer(Employee):
    def work(self):
        b = super().work()
        b = b[:-1] + ' start hiring'
        return b

    def __str__(self):
        return 'Должность: иvя или фамилия ' + self.full_name

`
class Recruiter(Employee):
    def work(self):
        a = super().work()
        a = a[:-1] + ' start coding'
        return a


class Vacancy:
    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level


class Candidate :
    def __init__(self, full_name, email, technologies, main_skill, main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    def work(self):
        raise UnableToWorkException()
