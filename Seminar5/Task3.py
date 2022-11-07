# Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. 
# Удалите все повторяющиеся элементы.

from random import randint

numbers = []
for i in range(10):
    numbers.append(randint(1, 10))

def sort_elements(numbers:list): return list(filter(lambda x: numbers.count(x) == 1, numbers))  

print(numbers)
no_repeat_numbers = sort_elements(numbers)
print('Список уникальных элементов:\n', *no_repeat_numbers)
print(f'Сколько элементов совпадают: {(len(numbers)-len(no_repeat_numbers))}')