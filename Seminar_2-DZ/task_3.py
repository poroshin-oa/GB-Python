# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

input_int = int(input("Insert integer> "))

result_list = []

for i in range(1, input_int + 1):
    result_num = round((1+1/i)**i, 2)
    result_list.append(result_num) 

print(f"Result list: {result_list}")

result_sum = 0
result_list_length = len(result_list)

for i in range(result_list_length):
    result_sum += result_list[i]

print(f"Result sum: {result_sum}")