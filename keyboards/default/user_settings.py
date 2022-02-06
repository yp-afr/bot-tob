from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data.config import BUTTONS


async def get_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.insert(KeyboardButton(BUTTONS.get("go_back")))
    markup.insert(KeyboardButton(BUTTONS.get("add_user")))

    return markup