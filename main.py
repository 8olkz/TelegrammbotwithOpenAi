import openai
import aiogram
import requests
import tkinter as tk
from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor




token = '6052676464:AAFnIMLiEEgBznRw5RN-x0qLFSYLOBDFQdQ'
openai.api_key = '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'
modelid ="CompVis/stable-diffusion-v1-4"

bot1= Bot(token)
dp = Dispatcher(bot1)




@dp.message_handler(commands=['zapros'])
async def send(message : types.message):
    response = openai.Completion.create(
  model="text-davinci-003",
  prompt=message.text,
  temperature=1,
  max_tokens=2000,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["You:"]
)

    await message.answer(response['choices'][0]['text'])

@dp.message_handler(commands=['helpa'])
async def sendhelpa(message: types.message):
    await message.answer("Небольшая инструкция для работы с ботом.\nДля создание вопроса искусственному интеллекту напишиие: \n*/zapros + интерисующий вас вопрос*\n */img + описание картинки*")
  
@dp.message_handler(commands=['img'])
async def sendimage(message: types.message):
    resonse1 = openai.Image.create(
        prompt= message.text,
        size="1024x1024"
    )
    await message.answer(resonse1)

executor.start_polling(dp, skip_updates=True)

