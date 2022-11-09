# Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число.
# Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.

from random import randint

array = []
for i in range(15):
    array.append(randint(1, 10))

print(array)

number = list(map(int, input('Введите трёхзначное натуральное число: ')))
print(number)

for i in range(len(array)-3):
    if array[i:i+3] == number:
        print('Да')
        break
else:
    print('Нет')
