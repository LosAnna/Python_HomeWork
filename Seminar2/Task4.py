# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Сдвиньте все элементы списка на 2 позиции вправо.

N = input("Введите число: ")
N = int(N)

lst = (list (range (-N, N+1)))
print(lst)
print()
n = 2
print(lst[-n:] + lst[:-n])

