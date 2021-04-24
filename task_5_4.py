NUMBERS_TABLE = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [number for i, number in zip(NUMBERS_TABLE, NUMBERS_TABLE[1:]) if number > i]
print(result)
