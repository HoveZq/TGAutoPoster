from config import ACCESS_TOKEN
from revChatGPT.V1 import AsyncChatbot

async def retext(txt):
    chatbot = AsyncChatbot(config={
    "access_token": ACCESS_TOKEN
    })
    async for data in chatbot.ask(f'Сократи текст на русском до 100 символов. Количество символов не пиши: {txt}'):
        message = data["message"]
    return message