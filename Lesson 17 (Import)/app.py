from .custom import Programmer


def validate(employees):
    emails = []
    for i in employees:
        emails.append(i.email)
    unique = set(emails)
    if len(unique) != len(emails):
        raise ValueError


def main():
    ivan = Recruiter('Vanya', 730866, 300, 'vanya@gmail.com')
    alex = Programmer('Alex', 730966, 300, 'alex@gmail.com')
    dima = Programmer('Dima', 730866, 300, 'dima@gmail.com')
    kirill = Candidate('Kirill', 9379992, 255, 'kirill@gmail.com')
    validate([ivan, alex, dima, kirill])


if __name__ == '__main__':
    main()