from telethon import TelegramClient, events
import asyncio

api_id = 37131412
api_hash = 'b4d6fbf9fbe52b119320daeabb6ccd4'
bot_token = '8685711484:AAH6-b42wGzNxZf3Brb4pk4xH62NLKQYHjo'

client = TelegramClient('crash_bot', api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    text = event.raw_text
    if not text.startswith('@'):
        return
    username = text.split()[0].lstrip('@')
    try:
        user = await client.get_entity(username)
        await client.send_file(user, b'', voice_note=True, duration=0)
        await event.reply(f'Краш-сигнал отправлен @{username}')
    except Exception as e:
        await event.reply(f'Ошибка: {e}')

async def main():
    await client.start(bot_token=bot_token)
    await client.run_until_disconnected()

asyncio.run(main())
