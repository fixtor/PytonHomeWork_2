# Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

number = int(input("Введите число N: "))
list_number = {}
count = 0
for i in range(1, number+1):
    list_number[i] = int(round((1 + 1 / i) ** i, 0))
    count = count + list_number[i]
print(list_number, count)
