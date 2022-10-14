# Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.

number = input("Введите целое число: ")
number = int(number)

for i in range (1, number + 1, 1):
    if not (i % 2):
        print(i)