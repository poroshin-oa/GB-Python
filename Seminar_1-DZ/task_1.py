# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

input_day_number = int(input("Input day number> "))

if input_day_number == 6 or input_day_number == 7:
    print("This is weekend.")
elif input_day_number in range(1, 6):
    print("This is weekday.")
else:
    print("Error!")