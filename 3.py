a = int(input('Введите год: '))

if a % 4 != 0:
    print('Год не високосный.')

elif year % 100 == 0:
    if year % 400 == 0:
        print('Год високосный.')
    else:
        print('Год не високосный.')
else:
    print('Год високосный.')
