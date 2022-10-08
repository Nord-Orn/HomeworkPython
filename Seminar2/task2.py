# Задача2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

print()
number = int(input("Введите вещественное число: "))
pro = 1
list = []
r = range(1, number) 
if number >= 1:     
    for i in range(1, number+1):
        pro *= i
        list.append (pro)
    print("Массив: ", list)
elif number < 1:
    i = 1
    while i > number-1:
        pro *= i
        list.append (pro)
        i -=1
    print("Массив: ", list)  
print()


   