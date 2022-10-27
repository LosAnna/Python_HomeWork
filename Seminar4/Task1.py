# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = input("Введите число: ")
number = int(number)

i = 2 
lst = []
N = number
while i <= number:
    if number % i == 0:
        lst.append(i)
        number //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {N}: {lst}")