def sum_digits(n):
    summa = 0

    while n > 0:
        summa += n % 10
        n //= 10

    return summa


odd_numbers = list(range(1, 1000, 2))
cubes = list(map(lambda i: pow(i, 3), odd_numbers))
print('Список кубов чисел:', cubes)

resultA = sum(filter(lambda n: sum_digits(n) % 7 == 0, cubes))
resultB = sum(filter(lambda n: sum_digits(n + 17) % 7 == 0, cubes))

print('Сумма цифр, которые нацело делятся на 7:', resultA)
print('Сумма цифр, увеличенного на 17 списка, которые нацело делятся на 7:', resultB)


