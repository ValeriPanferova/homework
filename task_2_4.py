PHRASE = 'На заводе работает {}'

employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита']

for el in employees:
    lst_employees = el.split()  # разделяем элементы на список подстрок
    employees_names = lst_employees[-1]  # берем последний элемент в списке - имена сотрудников
    employees_names = employees_names.title()  # с заглавной буквы пишем имена сотрудников
    print(PHRASE.format(employees_names))  # подставляем имена сотрудников в текст
