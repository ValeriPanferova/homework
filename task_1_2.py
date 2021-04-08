# 1. Создание списка состоящегои из кубов нечетных числе от 1 до 1000
lst_odd_numbers = []
sum_numbers = 0  # переменная, куда сохраняем сумму числа из списка

for i in range(1, 1001):  # генерируем числа от 1-1000
    if i % 2 != 0:  # если число не четное
        lst_odd_numbers.append(i ** 3)  # сгенерируемое число сохраняется в список возведенное в куб
print(lst_odd_numbers)

# 2. Вычисление суммы тех чисел из списка, сумма цифр которых делится нацело на 7
# for number in lst_odd_numbers:
#     while number >= 10:  # условие выполняется пока число больше или равно 10
#         sum_numbers += number % 10  # получение последней цифры числа
#         number = number // 10  # уменьшение числа на один разряд
#     if number < 10:  # если число меньше 10, то прибавляем число в переменную sum_numbers
#         sum_numbers += number
#     if sum_numbers % 7 == 0:  # если сумма числа делится нацело на 7, выводим на печать
#         print(sum_numbers)
#     sum_numbers = 0  # обнуление переменной sum_numbers для последующего вычисления списка

# 3. Добавление числа 17 и вычисление чисел из списка, сумма цифр которых делится нацело на 7
for number in range(len(lst_odd_numbers)):  # к каждому элементу списка добавляем число 17
    lst_odd_numbers[number] += 17
print(lst_odd_numbers)

for number in lst_odd_numbers:
    while number >= 10:
        sum_numbers += number % 10
        number = number // 10
    if number < 10:
        sum_numbers += number
    if sum_numbers % 7 == 0:
        print(sum_numbers)
    sum_numbers = 0
