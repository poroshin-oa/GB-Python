# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ⋀ - and
# ⋁ - or
# ¬ - not

predicate_array_names = ["X", "Y", "Z"]
predicate_range = [0, 1]
predicate_array = []

for i in range(3):
    predicate_input = int(input("Input {}> ".format(predicate_array_names[i])))
    
    if predicate_input not in predicate_range:
        print("Error!")
        break
    else:
        predicate_array.append(predicate_input)

left = not (predicate_array[0] or predicate_array[1] or predicate_array[2])
right = not predicate_array[0] and not predicate_array[1] and not predicate_array[2]
result = left == right

print(result)