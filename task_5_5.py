NUMBERS_TABLE = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique_numbers = [number for number in NUMBERS_TABLE if NUMBERS_TABLE.count(number) == 1]
print(unique_numbers)
