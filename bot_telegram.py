from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

'''******************************КЛИЕНТСКАЯ ЧАСТЬ*******************************************'''


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\n https://t.me/InterestDate_Bot')


'''*******************************АДМИНСКАЯ ЧАСТЬ*******************************************'''

'''*********************************ОБЩАЯ ЧАСТЬ*********************************************'''


@dp.message_handler()
async def echo_send(message: types.Message):
    if message.text == 'Привет':
        await message.answer('И тебе привет')
    # await message.answer(message.text)
    # await message.reply(message.text)
    # Работает только если бот уже знает о пользователе
    # await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates=True)
