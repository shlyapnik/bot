from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from utils.misc import rate_limit

from loader import dp

# @rate_limit(limit=10) #включаем лимит на отправку команды /start
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!') #Имя юзера
