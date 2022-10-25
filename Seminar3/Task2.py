#  В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.

letter = input("Введите заглавную букву: ")

with open('fruits.txt', encoding='utf-8') as fin:
    for line in fin:
        for word in line.split():
            if letter in word [0]:
                print(word)

