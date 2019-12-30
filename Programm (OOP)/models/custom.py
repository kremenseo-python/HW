from .employee import Employee


class Programmer(Employee):
    def work(self):
        b = super().work()
        b = b[:-1] + ' start hiring'
        return b

    def __str__(self):
        return 'Должность: иvя фамилия' + self.full_name


class Recruiter(Employee):
    def work(self):
        a = super().work()
        a = a[:-1] + ' start coding'
        return a
