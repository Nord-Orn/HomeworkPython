#  Напишите программу, которая принимает на вход координаты двух 
# точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
xa = int(input("Введите X первой координаты: "))
ya = int(input("Введите Y первой координаты: "))
xb = int(input("Введите X второй координаты: "))
yb = int(input("Введите Y второй координаты: "))
print("Расстояние между точками: ", round(((xa - xb)**2 + (ya - yb)**2)**(1 / 2), 2))
