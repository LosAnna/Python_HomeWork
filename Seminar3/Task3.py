# Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. 
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.

from random import choice
f = open('dictionarybot.txt', 'r', encoding='utf-8')
d = {}
for line in f:
    d[line[:line.index('==')-1]] = line[3+line.index('=='):].split('\\')
f.close()
 
response = input()
for key in d.keys():
    if response.lower() in key:
        print(choice(d[key]))
        break
else:        
    print('Уточните, я Вас не понимаю')
        
    