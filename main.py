from aiogram import Bot
from config import TOKEN, CHANNELS_ID
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
from DataBase import database
from Parser import get_links, get_text, retext
database = database()
bot = Bot(TOKEN, parse_mode='html')

async def main():
    #Получение ссылок
    links = await get_links(database)
    for link in links:
        #Получение текста в ссылках
        txt = await get_text(link)
        if txt != '':
            #ChatGPT
            retexted = await retext(txt)
            for channel in CHANNELS_ID:
                await bot.send_message(channel, text=retexted, disable_web_page_preview=True)
        
if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    apscheduler = AsyncIOScheduler(event_loop=loop, timezone='Europe/Moscow')
    apscheduler.add_job(main, 'interval', minutes=30, next_run_time=datetime.now()) #Интервал проверки постов
    apscheduler.start()
    loop.run_forever()