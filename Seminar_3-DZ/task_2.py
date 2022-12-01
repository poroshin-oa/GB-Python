# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def set_list_length(input_list):
    input_list_length = len(input_list)

    if input_list_length % 2 != 0:
        input_list_length = input_list_length // 2 + 1
    else:
        input_list_length = input_list_length // 2

    return input_list_length


def multiply_list(inp_list, list_length):
    result_list = []

    for i in range(list_length):
        result_list.append(inp_list[i] * inp_list[len(inp_list) - i - 1])

    return result_list


my_list = [2, 3, 4, 5, 6]
my_list_len = set_list_length(my_list)
mult_list = multiply_list(my_list, my_list_len)

print(mult_list)