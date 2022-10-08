# Задача 5. Реализуйте алгоритм перемешивания списка.

import random 

list = []
N = int(input("Введите число: "))
lst = []
for i in range(N):
    list.append(random.randint(1, 20))
print("Список: ", list)
random.shuffle(list)
print("Список после перемешивания:", lst)