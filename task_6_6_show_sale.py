import sys

with open('bakery.csv', "r", encoding="utf-8") as file:
    if len(sys.argv) == 2:
        argument_1 = int(sys.argv[1])
        argument_2 = -1
        while argument_1 != 1:
            file.readline()
            argument_1 -= 1
    if len(sys.argv) == 3:
        argument_1 = int(sys.argv[1])
        argument_2 = int(sys.argv[2])
        i = argument_1
        while i != 1:
            file.readline()
            i -= 1

    line = file.readline().strip()
    while line and argument_1 != argument_2+1:
        print(line)
        line = file.readline().strip()
        argument_1 += 1
