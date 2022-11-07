# Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.

from random import randint

numbers = []
for i in range(10):
    numbers.append(randint(1, 10))
    

def sort_elements(numbers): return filter(lambda x: x > 5, numbers)
print (numbers)  
print('Элементы из списка больше 5:\n', *sort_elements(numbers))