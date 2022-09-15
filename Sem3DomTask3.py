#3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части 
# элементов.

#*Пример:*

#- [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# - [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

import SemLib as name
'''
найдем разницу между max и min дробной части:
'''
def list_float(sp1):
    for i in range(len(sp1)):
        str_i = str(sp1[i])
        int_i = int(str_i.split(".")[1])
        if i == 0:
            max = int_i
            min = int_i
        else:
            if max < int_i:
                max = int_i
            if min > int_i:
                min = int_i
    return(max-min)                     

kol = name.kolich()  #Введем количество элементов
area = name.spisok_float(kol) #Введем список
area_float = list_float(area) #найдем разницу между max и min дробной части
name.print_list(area)
print(f'=> {area_float}',end=' ')
print()