import sys

with open('bakery.csv', "a+", encoding="utf-8") as f:
    numbers = sys.argv[1]
    f.writelines(numbers + '\n')

