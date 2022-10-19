# Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

line1 = input("Введите первую строку: ")
line2 = input("Введите вторую строку: ")

for element in set(line1):
    print(element,': ', line2.count(element))