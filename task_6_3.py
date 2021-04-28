import json
import sys


txt_users_name = ["Горбачёв Рудольф Давидович,\n", "Ершова Магда Георгьевна,\n", "Кудряшов Евгений Христофорович,\n",
                  "Колесникова Эллада Семеновна,\n", "Филиппов Андрей Мэлсович,\n", "Игнатьева Калерия Богуславовна,\n"]
txt_hobby_name = ["стрельба,\n", "выращивание растений,\n", "баскетбол,\n", "астрономия,\n", "косплей,\n",
                  "разработка сайтов,\n"]
with open('users.csv', "w", encoding="utf-8") as f, open('hobby.csv', "w", encoding="utf-8") as f2:
    f.writelines(txt_users_name)
    f2.writelines(txt_hobby_name)


def get_dictionary():
    with open('users.csv', "r", encoding="utf-8") as f_users, open('hobby.csv', "r", encoding="utf-8") as f_hobby:
        params_dictionary = {}
        key = f_users.readline().split(",")[0]
        value = f_hobby.readline().split(",")[0]
        while key:
            if value != '':
                params_dictionary.setdefault(key, value)
            else:
                params_dictionary.setdefault(key)
            key = f_users.readline().split(",")[0]
            value = f_hobby.readline().split(",")[0]
            if value != '' and key == '':
                sys.exit(1)
        return params_dictionary


get_dictionary()


params_as_str = json.dumps(get_dictionary())
with open("params.json", "w", encoding="utf-8") as f_params:
    json.dump(params_as_str, f_params)

print(type(params_as_str), params_as_str)

