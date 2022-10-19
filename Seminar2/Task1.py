# Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.

number = input("Введите число: ")
number = int(number)

factorial = lambda x: ((x == 1) and 1) or x * factorial(x - 1)
list2 = list(factorial(i) for i in range(1, number + 1))

print(list2)
