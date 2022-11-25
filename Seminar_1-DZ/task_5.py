# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

coordX_1 = int(input("Input X-1 coordinate> "))
coordY_1 = int(input("Input Y-1 coordinate> "))

coordX_2 = int(input("Input X-2 coordinate> "))
coordY_2 = int(input("Input Y-2 coordinate> "))

coordDistance = ((coordX_2 - coordX_1) ** 2 + (coordY_2 - coordY_1) ** 2) ** 0.5

print("Distance between point: {}".format(round(coordDistance, 2)))

