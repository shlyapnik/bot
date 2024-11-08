from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, bot
from aiogram.utils.markdown import hbold, hcode, hitalic, hunderline, hstrikethrough, hlink


@dp.message_handler(Command("parse_mode_html"))
async def show_parse_mode(message: types.Message):
    html_text = "\n".join(
        [
            "Привет, " + hbold(f"{message.from_user.full_name}"),
            "Как говорится:",
            hitalic("Бояться надо не смерти, а пустой жизни."),
            "",
            "Но мы сейчас не об этом. " + hstrikethrough("Что тебе нужно?"),
            "Этот текст с HTML форматированием. "
            "Почитать об этом можно " + hlink("тут",
                                              "https://core.telegram.org/bots/api#formatting-options"),
            hunderline("Внимательно прочти и используй с умом!"),
            "",
            hcode("Пример использования - ниже:"),
            "",
            ""
        ]
    )

    html_text += hcode(html_text)

    await message.answer(html_text, parse_mode=types.ParseMode.HTML)