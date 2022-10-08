 # Задача №3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным ементов.
# значением дробной части эл
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def rand_list(N):
    l = []
    for i in range(N):
        s = random.uniform(1,10) * 10000 // 100 / 100
        l.append(s)
    print(" Список: ", l)
    return l
    
def min_max(N):
    l = []
    s = len(N)
    min = 99
    max = 0
    for i in range(s):
        v = round(((N[i] * 100) % 100))
        l.append(v)
        if l[i] > 0 and l[i] < min: min = l[i]
        elif l[i] > max: max = l[i]
    print("Итоговая разница",((max - min)/100))

X = int(input("Введите число \n X = "))
L = rand_list(X)
min_max(L)
