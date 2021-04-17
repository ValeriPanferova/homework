def thesaurus(*args):
    names = dict()  # создаем словарь
    for el in args:
        key = el[0]  # получаем ключ
        if names.get(key):
            names[key].append(el)  # если ключ есть, то добавляем в  словарь имя
        else:
            names.setdefault(key, [el])  # если ключа нет, то создаем пару ключ:значение
    return names


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
