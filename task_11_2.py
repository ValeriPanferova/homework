class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    user_num_1 = int(input('Введите делимое: '))
    user_num_2 = int(input('Введите делитель: '))
    if user_num_2 == 0:
        raise OwnError('На ноль делить нельзя!')
    print(f'Результат: {int(user_num_1 / user_num_2)}')
except ValueError:
    print('Вы ввели не число!')
except OwnError as err:
    print(err)
