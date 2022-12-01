# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


# С отрицательными индексами не вышло =((
fib_index = int(input("Insert fibonacci index> "))

def fibonacci_plus(index):
    fib_int1 = fib_int2 = 1

    fib_plus_list = [fib_int1, fib_int2]
    
    for i in range(2, index):
        fib_int1, fib_int2 = fib_int2, fib_int1 + fib_int2
        fib_plus_list.append(fib_int2)

    return fib_plus_list

print(fibonacci_plus(fib_index))