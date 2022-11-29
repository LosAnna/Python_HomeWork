# Дана квадратная матрица, заполненная случайными числами. Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.

import random as rd

rows = columns = 3
sumDiagonal = 0
count = 0
numbers = [0] * rows 
rowNum = 1

for i in range(len(numbers)):
    numbers[i] = list(0 for _ in range(columns))

for i in range(rows):
    for j in range(columns):
        current_number = rd.randint(0,10)
        numbers[i][j] = rd.randint(0,10)
        if i == j:
            sumDiagonal += numbers[i][j]
        
print("\nKвадратная матрица, заполненная случайными числами:")
for row in numbers:
    print(row)

print(f'\nCуммa главной диагонали: {sumDiagonal}')  

for i in range(rows):
    for j in range(columns):
        count += numbers[i][j]
    if count > sumDiagonal:
        print(f'Сумма элементов {rowNum} строки: {count} - больше суммы главной диагонали')
    count = 0
    rowNum += 1


