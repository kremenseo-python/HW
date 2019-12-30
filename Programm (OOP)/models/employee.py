class Employee:
    def __init__(self, full_name, phone, salary_day):
        self.full_name = full_name
        self.phone = phone
        self.salary_day = salary_day

    def work(self):
        return 'I come to the office.'

    def check_salary(self, days=None):
        if days is None:
            days = self.workdays()
        return self.salary_day * days

    def __lt__(self, other):
        return self.salary_day > other.salary_day
