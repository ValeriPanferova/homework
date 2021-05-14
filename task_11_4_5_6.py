class OfficeEquipment:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.res = {'Модель устройства': self.name, 'Цена за единицу': self.price, 'Количество': self.quantity}

    def income(self):
        try:
            name = input(f'Введите наименование: ')
            price = int(input(f'Введите цену за единицу: '))
            quantity = int(input(f'Введите количество: '))
            res = {'Модель устройства': name, 'Цена за единицу': price, 'Количество': quantity}
            self.res.update(res)
            print(self.res)
        except ValueError:
            print('Некорректные данные!')


class Printer(OfficeEquipment):
    pass


class Scanner(OfficeEquipment):
    pass


class Xerox(OfficeEquipment):
    pass


printer = Printer('Hp', 2, 300)
scanner = Scanner('Canon', 54000, 10)
xerox = Xerox('Xerox', 7000, 15)
printer.income()
scanner.income()
xerox.income()
