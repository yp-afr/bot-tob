from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

first_names_cd = CallbackData("select_first_name", "value")
middle_names_cd = CallbackData("select_middle_name", "value")


async def get_first_names_keyboard(names_list):
    markup = InlineKeyboardMarkup(row_width=3)
    for name in names_list:
        markup.insert(InlineKeyboardButton(text=name, callback_data=first_names_cd.new(value=name)))
    return markup


async def get_middle_names_keyboard(names_list):
    markup = InlineKeyboardMarkup(row_width=2)
    for name in names_list:
        markup.insert(InlineKeyboardButton(text=name, callback_data=middle_names_cd.new(value=name)))
    return markup
