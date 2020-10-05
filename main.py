from time import sleep
import requests
from dotenv import load_dotenv
from os import getenv

load_dotenv()

TOKEN = getenv('token')
URL = URL = f"https://api.telegram.org/bot{TOKEN}/"


def get_updates_json(request):
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()


def last_update(data):
    print(data)
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id


def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(URL + 'sendMessage', data=params)
    return response


def main():
    update_id = last_update(get_updates_json(URL))['update_id']
    while True:
        if update_id == last_update(get_updates_json(URL))['update_id']:
            send_mess(get_chat_id(last_update(get_updates_json(URL))), 'привет')
            update_id += 1
        sleep(1)


if __name__ == '__main__':
    main()
