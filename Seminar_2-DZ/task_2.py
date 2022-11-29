# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

input_int = int(input("Insert integer> "))

result_int = 1
result_int_list = []

for i in range(1, input_int + 1):
    result_int *= i
    result_int_list.append(result_int)

print(result_int_list)