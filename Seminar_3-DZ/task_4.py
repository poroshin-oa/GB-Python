# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

inp_int = int(input("Insert integer: "))
result_binary = ""
while inp_int != 0:
    result_binary = str(inp_int % 2) + result_binary
    inp_int //= 2
print(result_binary)