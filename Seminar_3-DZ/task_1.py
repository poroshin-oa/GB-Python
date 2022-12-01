# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

original_list = [2, 3, 5, 9, 3, 5, 8, 11, 22]
original_list_length = len(original_list)

odd_elem_sum = 0

for i in range(1, original_list_length, 2):
    odd_elem_sum+=original_list[i]

print(f"Odd sum: {odd_elem_sum}")