# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

list = []
N = int(input("Введите число: "))
for i in range(N):
    list.append(randint(-N, N))
print("Список: ", list)
result = 1
f = open("file.txt", "r")
for line in f:
    result *= list[int(line)]
f.close()
print("Произведение элементов: ", result)