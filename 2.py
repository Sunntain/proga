def z1():
 num = False
 upc = False
 lowc = False
 sp = False
 pas1 = input('Введите пароль: ')
 for char in pas1:
     if char.isnumeric():
         num = True
     elif char.isupper():
         upc = True
     elif char.islower():
         lowc = True
     elif char in "!@#$%^*":
         sp = True
 if len(pas1) > 5 and num and upc and lowc and sp:
     print('oк')
 elif len(pas1) <= 5:
     print('слишком короткий пароль')
 elif num == False:
     print('добавьте цифры')
 elif upc == False:
     print('добавьте большие буквы')
 elif lowc == False:
     print('добавьте маленькие буквы')
 elif sp == False:
     print('добавьте специальные символы')

def z2():
    mesto = int(input('Введите номер места: '))
    if mesto % 2 == 0:
        if mesto in range(1, 37):
            print('Верхнее, купе')
        if mesto in range(37, 55):
            print('Верхнее, боковое')
    if mesto % 2 == 1:
        if mesto in range(1, 37):
            print('Нижнее, купе')
        if mesto in range(37, 55):
            print('Нижнее, боковое')
    if mesto < 1 or mesto > 54:
        print('Такого места нет')

def z3():
    g = int(input('Введите год: '))
    if (g % 4 == 0 and g % 100 != 0) or g % 400 == 0:
        print('Год', g, ' - високосный')
    else:
        print('Этот год не високосный')

def z4():
    a, b = input(), input()
    if a != 'красный' and a != 'синий' and a != 'желтый' or b != 'красный' and b != 'синий' and b != 'желтый':
        print('ошибка цвета')
    elif a == b:
        print(a)
    elif a == 'красный' and b == 'синий' or b == 'красный' and a == 'синий':
        print('фиолетовый')
    elif a == 'красный' and b == 'желтый' or b == 'красный' and a == 'желтый':
        print('оранжевый')
    elif a == 'синий' and b == 'желтый' or b == 'синий' and a == 'желтый':
        print('зеленый')