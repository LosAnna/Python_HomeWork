# Дан список случайных чисел. 
# Создайте список, в который попадают числа, описывающие возрастающую последовательность. Порядок элементов менять нельзя.

from random import randint

numbers = []
for i in range(10):
    numbers.append(randint(1, 10))

def sort_elements(numbers):
    result = [numbers[0]]
    for el in numbers:
        if el > result[-1]:
            result.append(el)
    return result    

print(numbers)
print('Список чисел с возрастающей последовательностью:\n', *sort_elements(numbers))    