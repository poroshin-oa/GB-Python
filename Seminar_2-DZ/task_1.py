# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 0,56 -> 11

float_input = input("Input float> ")

if float_input.find(",") > 0:
    separator = ","
elif float_input.find(".") > 0:
    separator = "."

float_no_separator = float_input.replace(separator, "")

float_number_sum = 0
float_number_length = len(float_no_separator)

for i in range(float_number_length):
    float_number_sum += int(float_no_separator[i])

print(float_number_sum)