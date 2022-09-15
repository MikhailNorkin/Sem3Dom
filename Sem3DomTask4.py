#4- Напишите программу, которая будет преобразовывать десятичное число в двоичное.

#*Пример:*

#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

'''
Проверка на правильность ввода числа
'''
def read_int():
    while True:
        try:
            num = int(input("Введите число в двоичной системе исчисления "))
            return num
        except ValueError:
            print("Вы не ввели число!")
'''
Перевод числа из десячной в двоичную сисему
'''
def change(number10):
    number2 = ''
    if number10 == 0:
        number2 = 0
    else:    
        while number10 > 0:
            number2 = str(number10%2)+number2
            number10 = number10//2            
    print(number2)

number10 = read_int()
change(number10)