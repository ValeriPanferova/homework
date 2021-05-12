class Cell:
    def __init__(self, cell_number):
        self.cell_number = int(cell_number)

    def __add__(self, other):
        return f'Размер клетки составляет: {self.cell_number + other.cell_number}'

    def __sub__(self, other):
        sub = self.cell_number - other.cell_number
        return f'Размер клетки уменьшился. Он стал равен: {sub} клеткам' if sub > 0 else 'Клетка исчезла'

    def __mul__(self, other):
        return f'Произведение двух клеток равно: {self.cell_number * other.cell_number}'

    def __truediv__(self, other):
        return f'Частное двух клеток равно: {self.cell_number // other.cell_number}'

    def make_order(self, row):
        result = ''
        for i in range(int(self.cell_number / row)):
            result += '*' * row + '\n'
        result += '*' * (self.cell_number % row) + '\n'
        return result


cell_1 = Cell(28)
cell_2 = Cell(15)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))
