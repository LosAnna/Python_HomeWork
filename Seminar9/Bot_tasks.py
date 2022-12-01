import telebot
import requests
import time
import random

global num
global count
count = 0
num = random.randint(1,1000)

bot = telebot.TeleBot("TOKEN", parse_mode=None)

@bot.message_handler(commands=['start', 'help', 'hello'])
def send_welcome(message):
	bot.reply_to(message, "Приветствую!Как Ваши дела?")


@bot.message_handler(content_types=['text'])
def hello_user(message):

    def Calc(message):
        if '+' in message.text or '-' in message.text or '/' in message.text or '*' in message.text:
            do = str(eval(str(message.text)))
            bot.send_message(message.chat.id, f'{do}')
        else:
            bot.send_message(message.chat.id, 'Команда не распознана, попробуйте снова!')     

    def Game(message):
        global num
        global count
        count +=1
        if int(message.text) > num:        
            a = bot.send_message(message.chat.id, "Загаданное число меньше!") 
            bot.register_next_step_handler(a, Game)
        elif int(message.text) < num:         
            b = bot.send_message(message.chat.id, "Загаданное число больше!") 
            bot.register_next_step_handler(b, Game)
        else:         
            bot.send_message(message.chat.id, f"Правильно, это число {num}. Вы угадали с {count} попытки!")           



    if 'привет' in message.text:
        bot.reply_to(message, "Привет, " + message.from_user.first_name)
    elif message.text == 'погода':
        r = requests.get('https://wttr.in?0T')
        bot.reply_to(message, r.text)
    elif message.text == 'котик':
        r = f'https://cataas.com/cat?t=${time.time()}'
        bot.send_photo(message.chat.id, r)
    elif message.text == 'файл':
        data = open('user_message.txt', encoding='utf-8')
        bot.send_document(message.chat.id, data)
        data.close()
    elif message.text == 'вычисли':
        r = bot.send_message(message.chat.id, 'Что необходимо вычислить?')
        bot.register_next_step_handler(r, Calc)
    elif message.text == 'играть':
        r = bot.send_message(message.chat.id, 'Я загадал число от 1 до 1000, попробуй его отгадать')
        bot.register_next_step_handler(r, Game)

    data = open('user_message.txt', 'a+', encoding='utf-8')
    data.writelines(str(message.from_user.id) + ' ' + message.text + '\n')
    data.close()



bot.infinity_polling()    