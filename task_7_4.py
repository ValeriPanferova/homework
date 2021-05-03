import os

DATA_FILE = r'C:\Users\V.Panferova\Desktop\Geekbrains\some_data'
list_size = []
dictionary = {10: 0, 100: 0, 1000: 0, 10000: 0, 100000: 0, 1000000: 0}

for i in os.listdir(DATA_FILE):
    list_size.append(os.stat(os.path.join(DATA_FILE, os.path.basename(i))).st_size)

list_size.sort(key=None, reverse=False)

for el in list_size:
    if el <= 10:
        dictionary[10] = dictionary.get(10) + 1
    elif el <= 100:
        dictionary[100] = dictionary.get(100) + 1
    elif el <= 1000:
        dictionary[1000] = dictionary.get(1000) + 1
    elif el <= 10000:
        dictionary[10000] = dictionary.get(10000) + 1
    elif el <= 100000:
        dictionary[100000] = dictionary.get(100000) + 1
    elif el <= 1000000:
        dictionary[1000000] = dictionary.get(1000000) + 1

print(dictionary)

