from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

show_records_cd = CallbackData("show_records", "type")


async def get_keyboard(type):
    markup = InlineKeyboardMarkup()
    markup.insert(InlineKeyboardButton(text="Показать", callback_data=show_records_cd.new(type=type)))
    return markup
