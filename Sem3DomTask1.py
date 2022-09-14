#1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

#*Пример:*

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

'''
ввод количества элементов в списке
'''
def kolich():
    while True:
        try:
            num = int(input("Введите количество элементов в списке "))
            return num
        except ValueError:
            print("Вы не ввели число!")

'''
ввод списка
'''
def spisok(kol_elements):
    sp=[]
    for i in range(kol_elements):
        sp.append(int(input(f"Введите {i} элемент списка: ")))
    return(sp)    

def find_sum(sp):
    sum = 0
    for i in sp:
        if i % 2 != 0:
            sum = sum + i
    print(f"Сумма элементов, стоящих на нечетных позициях равна: {sum}")
    
area = [2,3,5,9,3]

kol = kolich()
area = spisok(kol)
print(area)
find_sum(area)
