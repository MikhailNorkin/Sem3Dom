#-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#*Пример:*

#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

'''
Создадим новый список, который найдет произведение пар чисел
'''
def multiplication_list(sp1):
    sp2=[]
    for i in range(len(sp1)):
        sp2.append(sp1[i] * sp1[len(sp1)-i-1])
        if (i+1)*2>=len(sp1):
            break
    return sp2    
'''
Выведем список на экран
'''
def print_list(sp):
    print('[',end='')
    for i in range(len(sp)):
        if i+1 != len(sp):
            print(sp[i], end=", ")
        else:
            print(sp[i], end="")
        
    print(']',end=' ')
    print()
        

import SemLib as name
kol = name.kolich()  #Введем количество элементов
area = name.spisok(kol) #Введем список
new_area = multiplication_list(area) #Найдем произвдение пар чисел
print_list(new_area)
print()