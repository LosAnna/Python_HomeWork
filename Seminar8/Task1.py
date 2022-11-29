# В каждой группе учится от 20 до 30 студентов. 
# По итогам экзамена все оценки заносятся в таблицу. Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.

import random as rd

rows = 4
columns = rd.randint(20,30)
numbers = [0] * rows
count = 0
scores = 0
groupNum = 1
BestScore = 0
BestGroupNumber = 0

for i in range(len(numbers)):
    columns =  rd.randint(20,30)
    numbers[i] = list(0 for _ in range(columns))
    for j in range(columns):
        numbers[i][j] = rd.randint(1,5)
        count += numbers[i][j]
    scores = count / columns

    if BestScore < scores:
        BestScore = scores
        BestGroupNumber = groupNum
    print(f'Средний балл группы {groupNum}:')    
    print(scores)
    count = 0
    groupNum += 1

print('\nВсе группы:')
for row in numbers:
    print(row)

print(f'\nНаилучшая группа №{BestGroupNumber} со средним баллом {BestScore}')
