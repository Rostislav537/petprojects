from telethon import TelegramClient
import time

api_id=0
api_hash = ""

client=TelegramClient("test_tg", api_id, api_hash)

async def main():
    dialogs=await client.get_dialogs()
    for dialog in dialogs:
        if dialog.title=="Календарь событий":
            messages=client.iter_messages(dialog)
            async for msg in messages:

                text = msg.text
                if "#реклама" in text:
                    return


                time.sleep(1)

with client:
    client.loop.run_until_complete(main())
