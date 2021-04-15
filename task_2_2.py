lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+1.9', 'градусов']

lst_numbers = []

for el in lst:
    if el.isdigit():  # если строка состоит из цифр
        if el.isdecimal():  # если все символы в строке являются десятичными
            if len(el) == 1:  # если длина элемента равна 1
                lst_numbers.append('"' + str(0) + el + '"')  # к элементу добавляется 0 и элемент обособляется ""
            else:
                lst_numbers.append('"' + el + '"')  # если длина элемента не равна 1, то элемент обособляется ""
    elif el.startswith('-') or el.startswith('+'):  # если элемент начинается со знака + или -
        el_slice = el[1:]  # исключаем первый символ в строке
        if el_slice.isdecimal():  # если символы в строке десятичные
            if len(el_slice) == 1:  # если длина элемента равна 1
                lst_numbers.append('"' + el[0] + str(0) + el_slice + '"')  # значение добавляем в список
            else:
                lst_numbers.append('"' + el + '"')  # если длина элемента не равна 1, то элемент обособляется ""
        else:
            lst_numbers.append(el)  # если элементы в строке не десятичные, то элемент не обособляется ""
    else:
        lst_numbers.append(el)

print(lst_numbers)
