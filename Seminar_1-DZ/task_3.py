# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

coordX = int(input("Input X coordinate> "))
coordY = int(input("Input Y coordinate> "))
quarterNumber = 0

if coordX == 0 or coordY == 0:
    print("Error! Coordinates cannot be 0")
else:
    if coordX > 0 and coordY > 0:
        quarterNumber = 1
    elif coordX < 0 and coordY > 0:
        quarterNumber = 2
    elif coordX < 0 and coordY < 0:
        quarterNumber = 3
    elif coordX > 0 and coordY < 0:
        quarterNumber = 4
    else:
        print("Coordinates value error!")

print("Quarter number is: {}".format(quarterNumber))