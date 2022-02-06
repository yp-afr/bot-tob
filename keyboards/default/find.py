from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data.config import BUTTONS


async def get_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.insert(KeyboardButton(BUTTONS.get("by_name")))
    #markup.insert(KeyboardButton(BUTTONS.get("settings")))
    markup.row(BUTTONS.get("go_back"))
    return markup
