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
ввод списка целых чисел
'''
def spisok(kol_elements):
    sp=[]
    for i in range(kol_elements):
        sp.append(int(input(f"Введите {i} элемент списка: ")))
    return(sp) 
'''
ввод списка вещественных чисел
'''
def spisok_float(kol_elements):
    sp=[]
    for i in range(kol_elements):
        sp.append(float(input(f"Введите {i} элемент списка: ")))
    return(sp) 
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
