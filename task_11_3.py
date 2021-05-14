class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


result = []
while True:
    value = input('Введите число для добавления в список или exit для выхода: ')
    if value == 'exit':
        print(f'Сформированный вами список: {result}')
        break
    try:
        if not value.isnumeric():
            raise MyError('NaN')
        result.append(int(value))
    except MyError as error:
        print('Вы ввели не число')
