import requests


def get_updates_json(request):
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()


def send_mess(request, chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(request + 'sendMessage', data=params)
    return response
