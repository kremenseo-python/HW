class Employee:
    """Определяем класс сотрудников"""
    def __init__(self, full_name, phone, salary_day, email):
        self.full_name = full_name
        self.phone = phone
        self.salary_day = salary_day
        self.validate(email)
        self.email = email
        self.save_email_to_file()

    def validate(self, mail):
        print(self.get_email_from_file())
        if mail in self.get_email_from_file():
            raise ValueError

    def save_email_to_file(self):
        """Сохраняем эмейлы в файл"""
        with open('emails', 'a') as f:
            f.write(self.email)
            f.write('\n')

    def get_email_from_file(self):
        with open('emails', 'a+') as f:
            f.seek(0)
            data = f.read()
        return data.split('\n')

    def work(self):
        return 'I come to the office.'

    # def check_salary(self, days=None):
    #     if days is None:
    #         days = self.workdays()
    #     return self.salary_day * days

    def __lt__(self, other):
        return self.salary_day > other.salary_day