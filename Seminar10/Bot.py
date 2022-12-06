import telebot
from telebot import types
import datetime


is_started_question = False
is_started_answer = False

bot = telebot.TeleBot("5805302841:AAFwhmruEuHxB0HPOiGr-xp4dgzk3IZCDYI")

markup = types.ReplyKeyboardMarkup()
itembth1 = types.KeyboardButton('Привет')
itembth2 = types.KeyboardButton('Обращение')
itembth3 = types.KeyboardButton('Ответить на обращение')
markup.add(itembth1, itembth2, itembth3)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Привет, " + message.from_user.first_name, reply_markup=markup)

@bot.message_handler(content_types=["text"])
def hello_user(message):
    global is_started_question
    global is_started_answer
    if is_started_question:
        now = datetime.datetime.now()       
        data = open('user_question.txt','a+', encoding='utf-8')
        data.writelines(f"{str(message.from_user.id)} {message.from_user.first_name} {now.strftime('%d-%m-%Y %H:%M')}: {message.text} \n")
        data.close()
        bot.send_message(message.from_user.id, 'Ваше обращение отправлено!')
        is_started_question = False
    elif is_started_answer:
        data = open('user_question.txt','r+', encoding='utf-8')
        question = data.readline()
        data.close()
        user_id = question.split(' ')
        bot.send_message(user_id[0], message.text)                    
        is_started_answer = False
    else:        
        if 'Привет' in message.text:
            bot.reply_to(message, 'Привет, ' + message.from_user.first_name)
        elif message.text == 'Обращение':
                is_started_question = True
                bot.send_message(message.from_user.id, 'Введите ваше обращение')
        elif message.text == 'Ответить на обращение':
                is_started_answer = True
                data = open('user_question.txt','r+', encoding='utf-8')
                question = data.readline()
                data.close()
                bot.reply_to(message, question)
                bot.send_message(message.from_user.id, 'Введите ответ')
         
    
bot.infinity_polling()