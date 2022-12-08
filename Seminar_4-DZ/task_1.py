# Вычислить число c заданной точностью d

# Пример:

# - при d = 0.001, π = 3.141   
# Ввод: 0.01
#     Вывод: 3.14

#     Ввод: 0.001
#     Вывод: 3.141

from math import pi

float_input = input("Введите число для заданной точности числа Пи> ")

if float_input.find(",") == 1:
    float_list = float_input.split(",")
elif float_input.find(".") == 1:
    float_list = float_input.split(".")
else:
    print("Error!")

pi_precision = len(float_list[1])

print(f'число Пи с заданной точностью {pi_precision} равно {round(pi, pi_precision)}')