from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    def fabric_consumption(self):
        return f'Общий расход ткани составляет: {self.param / 6.5 + 0.5 * 2 * self.param + 0.3}'

    @abstractmethod
    def abstract(self):
        pass


class Coat(Clothes):
    def fabric_consumption(self):
        return f'Для пошива пальто нужно: {self.param / 6.5 + 0.5} ткани'

    def abstract(self):
        pass


class Suit(Clothes):
    def fabric_consumption(self):
        return f'Для пошива костюма нужно: {2 * self.param + 0.3} ткани'

    def abstract(self):
        pass


coat = Coat(85)
suit = Suit(30)
print(coat.fabric_consumption())
print(suit.fabric_consumption())
print(coat.abstract())
