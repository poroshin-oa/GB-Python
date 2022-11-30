# Реализуйте алгоритм перемешивания списка.

# Не придумал, как реализовать без повторений элементов - если циклом
# Если без цикла - решается в 2 строки, random.shuffle

import random

original_list = [i for i in range(10)]
original_list_length = len(original_list)

print(f"Original list: {original_list}")

random_list = []

for i in range(original_list_length):
    random_index = random.randint(0, original_list_length - 1)
    random_list.append(original_list[random_index])

print(f"Result list: {random_list}")