sec_in_day = 86400  # количество секунд в дне
sec_in_hour = 3600  # количество секунд в часе
sec_in_minute = 60  # количество секунд в минуте

duration = 674800  # продолжительность в секундах

if duration > sec_in_day:  # вычисляем дни, если duration больше 1 дня
    days = int(duration / sec_in_day)  # вычисляем сколько дней в duration
    remains_sec = duration % sec_in_day
    hours = int(remains_sec / sec_in_hour)  # из оставшихся секунд вычисляем сколько это часов
    remains_sec_hour = remains_sec % sec_in_hour
    minutes = int(remains_sec_hour / sec_in_minute)  # из оставшихся секунд вычисляем минуты
    remains_sec_minute = remains_sec_hour % sec_in_minute
    print(str(days), 'дн ' + str(hours), 'час ' + str(minutes), 'мин ' + str(remains_sec_minute), 'сек')
elif sec_in_day > duration > sec_in_hour:  # считаем часы, если duration больше 1 часа, но меньше 1 дня
    hours = int(duration / sec_in_hour)  # вычисляем сколько часов в duration
    remains_sec_hour = duration % sec_in_hour
    minutes = int(remains_sec_hour / sec_in_minute)  # из оставшихся секунд вычисляем минуты
    remains_sec_minute = remains_sec_hour % sec_in_minute
    print(str(hours), 'час ' + str(minutes), 'мин ' + str(remains_sec_minute), 'сек')
elif sec_in_hour > duration > sec_in_minute:  # считаем минуты, если duration больше 1 минуты, но меньше 1 часа
    minutes = int(duration / sec_in_minute)  # вычисляем сколько минут в duration
    remains_sec_minute = duration % sec_in_minute
    print(str(minutes), 'мин ' + str(remains_sec_minute), 'сек')
else:  # считаем количество секунд, если меньше 1 минуты
    print(str(duration), 'сек')
