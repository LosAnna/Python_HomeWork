# В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год. 
# Каждому месяцу соответствует своя строка. Определите самый жаркий и самый холодный 7-дневный промежуток этого периода. 
# Выведите его даты.

import random as rd

def NameOfMonth(month):
    if month == 1:
        month = 'май'
    elif month ==2:
        month = 'июнь'  
    elif month ==3:
        month = 'июль' 
    elif month ==4:
        month = 'август'
    elif month ==5:
        month = 'сентябрь'
    return month

months = 5
days = 31
numbers = [0] * months
june = 2 
september = 5
count = 1
step = []

warm = 0
cold = 999
monthWarm = 0
monthCold = 0
warmIndex = 0
coldIndex = 0

for i in range(len(numbers)):
    if count == 2 or count == 5:
        days =  30
    numbers[i] = list(0 for _ in range(days))
    for j in range(days):
        numbers[i][j] = rd.randint(10,30)
    for n in range(days-6):
        step = numbers[i][n:n + 7:1]
        _ = sum(step)
        if warm < _:
            warm = _
            monthWarm = count
            warmIndex = numbers[i][n]
            warmIndex = numbers[i].index(warmIndex)
        if cold > _:
            cold = _
            monthCold = count
            coldIndex = numbers[i][n]
            coldIndex = numbers[i].index(coldIndex)
    count += 1
    days =  31

print()
for months in numbers:
    print(months)

print(f'\nСамый жаркий месяц {NameOfMonth(monthWarm)} (с {warmIndex+1} по {warmIndex+7}), {warm} гр. ')
print(f'Самый холодный месяц {NameOfMonth(monthCold)} (с {coldIndex+1} по {coldIndex+7}), {cold} гр.')