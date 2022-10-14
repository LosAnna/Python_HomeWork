# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

number = input("Введите номер четверти от 1 до 4: ")
number = int(number)

if number == 1:
    print("X > 0 , Y > 0")
elif number == 2:
    print("X < 0 , Y > 0")
elif number == 3:
    print("X < 0 , Y < 0")
elif number == 4:
    print("X > 0 , Y < 0")
elif number < 1 or number > 4:
    print("Некорректное значение четверти")