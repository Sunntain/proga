def z1():
    try:
        x = int(input('введите число: '))
        y = x % 3
    except ValueError:
        print('введено не число')
    else:
        if y == 0:
            print(x, ' делится на 3')
        else:
            print(x, ' не делится на 3')

def z2():
    try:
        x = int(input('введите число: '))
        y = 100 / x
    except ValueError:
        print('введено не число')
    except ZeroDivisionError:
        print('введен 0 ')
    else:
        print('результат равен ', y)

def z3():
    x = input('введите дату в виде дд.мм.гг: ')
    x = x.split('.')
    y = int(x[0]) * int(x[1])
    if y == int(x[2]):
        print('дата магическая')
    else:
        print('дата не магическая')

def z4():
    x = input('введите номер билета: ')
    s1 = 0
    s2 = 0
    if len(x) % 2 == 0:
        for i in x[0:int((int(len(x))/2))]:
            s1 = s1 + int(i)
        for i in x[int((int(len(x))/2)):int(int(len(x)) + 1)]:
            s2 = s2 + int(i)
        if s1 == s2 :
            print('билет счастливый')
        else:
            print('билет не счастливый')
    else:
        print('введено нечетное количество символов')

z4()