from pprint import pprint
from time import sleep
import requests
from dotenv import load_dotenv
from os import getenv
from tbot_methods import get_updates_json, send_mess

load_dotenv()

TOKEN = getenv('token')
URL = f"https://api.telegram.org/bot{TOKEN}/"


def last_update(data):
    pprint(data)
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id


def is_this_bot_command(data):
    messages = len(data['result'])
    try:
        if data['result'][messages - 1]['message']['entities'][0]['type'] == 'bot_command':
            return True
    except (TypeError, KeyError):
        return False


def get_bot_command(data):
    messages = len(data['result'])
    try:
        return data['result'][messages - 1]['message']['text']
    except (TypeError, KeyError):
        print('Введи команду')


def main():
    data = get_updates_json(URL)
    update_id = last_update(data)['update_id']
    while True:
        data = get_updates_json(URL)
        if update_id == last_update(data)['update_id']:
            if is_this_bot_command(data):
                send_mess(URL, get_chat_id(last_update(data)), get_bot_command(data))
            update_id += 1
        sleep(5)


if __name__ == '__main__':
    main()

'''
добавить проверку на поле entities
Если приходит обычное сообщение, крашит
'''
