# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarterNumber = int(input("Insert quarter number> "))

if quarterNumber > 4 or quarterNumber <= 0:
    print("Error! Quarter number must be in the range 1-4")
else:
    if quarterNumber == 1:
        print("Range of X: 0 -> +infinity \nRange of Y: 0 -> +infinity")
    elif quarterNumber == 2:
        print("Range of X: 0 -> -infinity \nRange of Y: 0 -> +infinity")
    elif quarterNumber == 3:
        print("Range of X: 0 -> -infinity \nRange of Y: 0 -> -infinity")
    elif quarterNumber == 4:
        print("Range of X: 0 -> +infinity \nRange of Y: 0 -> -infinity")