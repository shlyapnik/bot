from aiogram.dispatcher.filters import Command
from loader import dp


@dp.message_handler(Command('start'))
async def echo(m):
    await m.answer(m.text)
