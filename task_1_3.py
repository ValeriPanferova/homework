list_percent = [' процент', ' процента', ' процентов']  # список склонений слова 'процент'

# 1. Ввод пользователем числа и вывод числа со склонением "процент".
ask_question = int(input('Введите число от 1-20: '))
if ask_question == 1:
    print(str(ask_question) + list_percent[0])  # вывод на печать числа 1 со склонением "процент"
elif 2 <= ask_question <= 4:
    print(str(ask_question) + list_percent[1])  # вывод на печать чисел от 2 до 4 склонением "процента"
else:
    print(str(ask_question) + list_percent[2])  # вывод на печать чисел от 5 до 20 склонением "процентов"

# 1.1 - Вывод склонения от 1 до 20.
for i in range(1, 21):  # генерируем числа от 1-20
    if i == 1:
        print(str(i) + list_percent[0])  # вывод на печать числа 1 со склонением "процент"
        i += 1
    elif 2 <= i <= 4:
        print(str(i) + list_percent[1])  # вывод на печать чисел от 2 до 4 склонением "процента"
        i += 1
    else:
        print(str(i) + list_percent[2])  # вывод на печать чисел от 5 до 20 склонением "процентов"
