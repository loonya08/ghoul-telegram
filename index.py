from config import *
from time import sleep
from telethon import TelegramClient, sync, events

client = TelegramClient('ghoul-session', api_id, api_hash)
client.start()

my_id = client.get_me().id

@client.on(events.NewMessage())
async def normal_handler(event):

    if(event.message.from_id.user_id == my_id and event.message.text == start_command):
        i = 1000
        while i > 0:
            sleep(sleep_time)
            await client.send_message(event.message.chat_id, str(i)+' - 7 = '+str(i-7))
            i -= 7
        await client.send_message(event.message.chat_id, end_message)

client.start()
client.run_until_disconnected()    