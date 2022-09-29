# Реализуйте алгоритм перемешивания списка.

n = int(input("Задайте список: "))
list_numbers = []
for i in range(n, n*2):
    list_numbers.append(i)
print(list_numbers)

list_numbers = [list_numbers[-1]] + list_numbers[:-1] # Переставляем последний элемент в начало
print(list_numbers)


    

