number = int(input('Введите число от 1 до 20:'))
if number <= 1:
    print(number, 'процент')
elif (number >= 1) and (number <= 4):
    print(number, 'процента')
elif (number > 4) and (number <= 20):
    print(number, 'процентов')
else:
    print(number, 'не входит в промежуток от 1 до 20')
    print('Справка: Им.п 1 - процент,', 'Им.п (2-4) - процента,', 'Им.п(6 - 20) - процентов.')