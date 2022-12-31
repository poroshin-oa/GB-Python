# Немного исправлено условие для демонстрации filter: ищется не сумма элементов на нечетных индексах,
# а сумма нечетных элементов

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

original_list = [2, 3, 5, 9, 3]
original_list_length = len(original_list)

odd_elem_sum = 0

odd_list = list(filter(lambda x: x%2 != 0, original_list))
odd_list_length = len(odd_list)


for i in range(0, odd_list_length):
    odd_elem_sum+=odd_list[i]


print(f"Odd sum: {odd_elem_sum}")