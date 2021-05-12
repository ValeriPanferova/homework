class Matrix:
    def __init__(self, list_1):
        self.list_1 = list_1

    def __str__(self):
        for row in self.list_1:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.list_1)):
            for i_2 in range(len(other.list_1[i])):
                self.list_1[i][i_2] = self.list_1[i][i_2] + other.list_1[i][i_2]
        return Matrix.__str__(self)


matrix = Matrix([[-2, 3, 1], [1, 0, 4], [0, 1, -1], [1, 2, -3]])
new_matrix = Matrix([[1, 0, 2], [-2, 0, 5], [0, 2, -11], [2, 3, -7]])
print(matrix.__add__(new_matrix))
