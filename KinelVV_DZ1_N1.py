duration = int(input('Введите значение в секундах: '))
if duration < 3600 and duration // 60 > 0:
    minuties = duration // 60
    seconds = duration % 60
    print(minuties, 'мин', seconds, 'сек')
elif (duration >= 3600) and (duration // 3600 > 0) and (duration < 86400):
    hours = duration // 3600
    minuties = (duration % 3600) // 60
    seconds = (duration % 3600) % 60
    print(hours, 'ч', minuties, 'мин', seconds, 'сек')
elif duration >= 86400 and duration // 86400 > 0:
    day = duration // 86400
    hours = (duration % 86400) // 3600
    minuties = ((duration % 86400) % 3600) // 60
    seconds = (duration % 86400) % 60
    print(day, 'дн', hours, 'ч', minuties, 'мин', seconds, 'сек')
else:
    print(duration, 'сек')


