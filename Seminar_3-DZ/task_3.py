# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

original_list = [1.1, 1.2, 3.4, 10.01, 10.12]

def get_fract_part(inp_list):
    inp_list_length = len(inp_list)
    fract_list = []

    for i in range(inp_list_length):
        fract_list.append(round(inp_list[i] % 1, 2))

    return fract_list

def get_diff_max_min(inp_fract_list):
    inp_fract_list_length = len(inp_fract_list)
    inp_fract_list_max = inp_fract_list[0]
    inp_fract_list_min = inp_fract_list[0]

    for i in range(inp_fract_list_length):
        if inp_fract_list[i] > inp_fract_list_max:
            inp_fract_list_max = inp_fract_list[i]
        elif inp_fract_list[i] < inp_fract_list_min:
            inp_fract_list_min = inp_fract_list[i]

    diff_max_min_elem = inp_fract_list_max - inp_fract_list_min

    return inp_fract_list_max, inp_fract_list_min, diff_max_min_elem


result_fract_list = get_fract_part(original_list)
result_fract_max_min = get_diff_max_min(result_fract_list)

print(f"List of fractional parts: {result_fract_list}")
print(f"Maximal element: {result_fract_max_min[0]}")
print(f"Minimal element: {result_fract_max_min[1]}")
print(f"Difference: {result_fract_max_min[2]}")