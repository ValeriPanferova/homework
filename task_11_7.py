class ComplexNumber:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    def __add__(self, other):
        return f'Сумма чисел: {self.number_1 + other.number_1} + {self.number_2 + other.number_2} * i'

    def __mul__(self, other):
        return f'Произведение чисел: {self.number_1 * other.number_1 - (self.number_2 * other.number_2)} + ' \
               f'{self.number_2 * other.number_1} * i'


complex_1 = ComplexNumber(8, -5)
complex_2 = ComplexNumber(2, 9)
print(complex_1 + complex_2)
print(complex_1 * complex_2)
