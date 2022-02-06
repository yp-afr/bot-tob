from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data.config import BUTTONS


async def get_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.insert(KeyboardButton(BUTTONS.get("find")))
    markup.insert(KeyboardButton(BUTTONS.get("settings")))

    return markup


