# Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
number = float(input("Введите вещественное число: "))
summa = 0
number *=100000
if number > 0:
    while number > 0:
        summa += number % 10
        number //= 10
else:
    number *= -1
    while number > 0:
        summa += number % 10
        number //= 10
print("Сумма цифр: ", round(summa))