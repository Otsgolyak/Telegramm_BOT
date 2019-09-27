import requests
import bot_info
import json
import time
import datetime
import random

token = bot_info.token

URL = "https://api.telegram.org/bot" + token + "/"

global last_update_id
last_update_id = 0


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()

    last_object = data['result'][-1]
    current_update_id = last_object['update_id']

    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id

        chat_id = last_object['message']['chat']['id']
        message_text = last_object['message']['text']

        message = {'chat_id': chat_id,
                   'text': message_text}


        return message
    return None


def send_message(chat_id, text='Wait please...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def main():
    # d = get_updates()

    # get_message()

    # with open('updates.json', 'w') as file:
    #     json.dump(d, file, indent=2, ensure_ascii=False)
    while True:
        answer = get_message()
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
                 'https://i.chzbgr.com/full/9309444352/h5DC0719B/',]

        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']

            if text in ['Привет', 'хай', 'ку', 'привет']:
                send_message(chat_id, 'Добрый день!')
            elif text in ['Как дела', 'как дела', 'как оно', 'чё как']:
                send_message(chat_id, 'Хорошо, а у вас?')
            elif text in ['Хорошо', 'збс', 'норм', 'хорошо']:
                send_message(chat_id, 'Рад за вас!')
            elif text in ['Как тебя зовут', 'ты кто', 'наховись', 'как тебя зовут']:
                send_message(chat_id, 'Гоша!')
            elif text in ['Который час', 'который час', 'время', 'сколько время']:
                current_time = datetime.datetime.now()
                send_message(chat_id, str(current_time))
            elif '+' in text:
                num_list = text.split('+')
                res = int(num_list[0]) + int(num_list[1])
                send_message(chat_id, str(res))
            elif '-' in text:
                num_list = text.split('-')
                res = int(num_list[0]) - int(num_list[1])
                send_message(chat_id, str(res))
            elif '*' in text:
                num_list = text.split('*')
                res = int(num_list[0]) * int(num_list[1])
                send_message(chat_id, str(res))
            elif '/' in text:
                num_list = text.split('/')
                res = int(num_list[0]) / int(num_list[1])
                send_message(chat_id, str(res))
            elif text in ['мем', 'покажи мем']:
                random_num = random.randint(0, 12)
                send_message(chat_id, memes[random_num])

        else:
            continue

        time.sleep(2)


if __name__ == "__main__":
    main()
