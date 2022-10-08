# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random


def rand_list(N):
    l = []
    for i in range(N):
        l.append(random.randint(1, 20))
    print(" Список: ", l)
    return l


def nev_list(l):
    X = len(l)
    list2 = []
    number = X - 1
    for i in range(X // 2):
        a = l[i] * l[number]
        list2.append(a)
        i += 1
        number -= 1
    if X % 2 == 1:
        a = l[X // 2]
        a **= 2
        list2.append(a)
    print(" Новый список: ", list2)


X = int(input("Введите \n X = "))
l = rand_list(X)
nev_list(l)
