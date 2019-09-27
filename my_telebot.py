import telebot
from telebot import types

import bot_info
import datetime
import random
import time

token = bot_info.token
bot = telebot.TeleBot("924145461:AAGBFMW9xwVXGSRBHaofiJ_QGuWIGmezfwg")



@bot.message_handler(content_types=['text'])
def send_text(message):
    memes = ['https://i.chzbgr.com/full/9340631296/h5D279EE0/',
             'https://i.chzbgr.com/full/9340629760/hC701B4F2/',
             'https://i.chzbgr.com/full/9340631552/h8C3349D4/',
             'https://i.chzbgr.com/full/9340631808/h72FA3616/',
             'https://i.chzbgr.com/full/9340632320/h83A8B60B/',
             'https://i.chzbgr.com/full/9340630784/h357E9FA4/',
             'https://i.chzbgr.com/full/9340630272/h30EC4472/',
             'https://i.chzbgr.com/full/9340633344/h8C284260/',
             'https://i.chzbgr.com/full/9340633600/h4CFEC57B/',
             'https://i.chzbgr.com/full/9309444608/h9E49B45A/',
             'https://i.chzbgr.com/full/9309448448/hD9122537/',
             'https://i.chzbgr.com/full/9309445888/h510F0C12/',
             'https://i.chzbgr.com/full/9309444352/h5DC0719B/', ]
    gif_memes = ['https://cdn.humoraf.ru/wp-content/uploads/2017/04/funniest-gifs-20.gif',
                 'https://cdn.humoraf.ru/wp-content/uploads/2017/04/funniest-gifs-22.gif',
                 'https://cdn.humoraf.ru/wp-content/uploads/2017/04/funniest-gifs-21.gif',
                 'https://cdn.humoraf.ru/wp-content/uploads/2017/04/funniest-gifs-23.gif',
                 'https://cdn.humoraf.ru/wp-content/uploads/2017/04/funniest-gifs-24.gif',
                 'https://cdn.humoraf.ru/wp-content/uploads/2017/04/funniest-gifs-28.gif',
                 'https://cdn.humoraf.ru/wp-content/uploads/2017/04/funniest-gifs-29.gif',
                 'https://cdn.humoraf.ru/wp-content/uploads/2017/04/funniest-gifs-30.gif',
                 'https://cdn.humoraf.ru/wp-content/uploads/2017/04/funniest-gifs-32.gif',
                 'https://cdn.humoraf.ru/wp-content/uploads/2017/04/funniest-gifs-33.gif',
                 'https://cdn.humoraf.ru/wp-content/uploads/2017/04/funniest-gifs-34.gif',
                 'https://cdn.humoraf.ru/wp-content/uploads/2017/04/funniest-gifs-35.gif',
                 'https://cdn.humoraf.ru/wp-content/uploads/2017/04/funniest-gifs-36.gif',
                 'https://cdn.humoraf.ru/wp-content/uploads/2017/04/funniest-gifs-37.gif',
                 ]
    if message.text == 'старт':
        while True:
            random_num = random.randint(0, 12)
            bot.send_message(message.chat.id, memes[random_num])
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Смотреть!", url="https://google.com")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Привет! Лушие предложения у нас!", reply_markup=keyboard)
            time.sleep(60)
    elif message.text in ['Привет', 'хай', 'ку', 'привет']:
        bot.send_message(message.chat.id, 'Добрый день!')
    elif message.text in ['Как дела', 'как дела', 'как оно', 'чё как']:
        bot.send_message(message.chat.id, 'Хорошо, а у вас?')
    elif message.text in ['Хорошо', 'збс', 'норм', 'хорошо']:
        bot.send_message(message.chat.id, 'Рад за вас!')
    elif message.text in ['Как тебя зовут', 'ты кто', 'наховись', 'как тебя зовут']:
        bot.send_message(message.chat.id, 'Гоша!')
    elif message.text in ['Который час', 'который час', 'время', 'сколько время']:
        current_time = datetime.datetime.now()
        bot.send_message(message.chat.id, str(current_time))
    elif message.text in ['Кто тебя создал', 'кто тебя создал']:
        bot.send_message(message.chat.id, 'Мой создатель Антон!')
    elif '+' in message.text:
        num_list = message.text.split('+')
        res = int(num_list[0]) + int(num_list[1])
        bot.send_message(message.chat.id, str(res))
    elif '-' in message.text:
        num_list = message.text.split('-')
        res = int(num_list[0]) - int(num_list[1])
        bot.send_message(message.chat.id, str(res))
    elif '*' in message.text:
        num_list = message.text.split('*')
        res = int(num_list[0]) * int(num_list[1])
        bot.send_message(message.chat.id, str(res))
    elif '/' in message.text:
        num_list = message.text.split('/')
        res = int(num_list[0]) / int(num_list[1])
        bot.send_message(message.chat.id, str(res))
    elif message.text in ['мем', 'покажи мем']:
        random_num = random.randint(0, 12)
        bot.send_message(message.chat.id, memes[random_num])
    elif message.text in ['гиф мем', 'покажи гиф мем']:
        random_num = random.randint(0, 13)
        bot.send_message(message.chat.id, gif_memes[random_num])


bot.polling(none_stop=True, interval=0)
