from models.custom import Programmer, Recruiter


def main():
    ivan = Recruiter('Vanya', 730866, 300)
    print(ivan.check_salary(10))
    print(ivan.work())
    dima = Programmer('Dima', 730866, 300)
    print(dima.check_salary(10))
    print(dima.work())
    print(dima)

    print(dima < ivan)


if __name__ == '__main__':
    main()