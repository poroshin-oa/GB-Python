# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

input_number = int(input("Insert N> "))
main_list = [i for i in range(-input_number, input_number)]
main_list_length = len(main_list)

print(f"Main List: {main_list}")

input_indexes_string = input("Insert indexes> ")
indexes_str_format = input_indexes_string.replace(" ", "")
indexes_str_length = len(indexes_str_format)

if indexes_str_length > main_list_length:
    print("Error! Number of indexes <= length of list")
else:    
    multiplication_result = 1
    
    for i in range(indexes_str_length):
        now_index = main_list[int(indexes_str_format[i])]
        multiplication_result *= now_index
    
    print(f"Result of indexes multiplication: {multiplication_result}")

    
    