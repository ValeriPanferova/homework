TUTORS = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']

KLASSES = ['9А', '7В', '9Б', '9В', '8Б']


def gen_of_people(i, j):
    grade = len(i) - len(j)
    if grade > 0:
        for _ in range(grade):
            j.append(None)
    for tutor, klass in zip(i, j):
        yield tutor, klass


my_generator = gen_of_people(TUTORS, KLASSES)
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
