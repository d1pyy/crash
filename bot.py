import requests
import time

TOKEN = '8685711484:AAH6-b42wGzNxZf3Brb4pk4xH62NLKQYHjo'
PAYLOAD = '%00' * 1500

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    requests.post(url, data={'chat_id': chat_id, 'text': text})

def get_updates(offset):
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    r = requests.get(url, params={'timeout': 30, 'offset': offset})
    return r.json()['result']

last = None
while True:
    updates = get_updates(last)
    for u in updates:
        last = u['update_id'] + 1
        msg = u.get('message')
        if not msg:
            continue
        text = msg.get('text', '')
        if text.startswith('@'):
            user = text.split()[0].lstrip('@')
            link = f'https://t.me/{user}?text={PAYLOAD}'
            send_message(msg['chat']['id'], link)
        else:
            send_message(msg['chat']['id'], 'Отправь @username')
    time.sleep(1)
