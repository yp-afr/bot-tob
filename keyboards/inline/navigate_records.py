from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

navigation_records_cd = CallbackData("navigation_records", "type", "iterator")


async def get_keyboard(type, iterator, data_len):
    markup = InlineKeyboardMarkup(row_width=2)
    next_iterator = (int(iterator) + 1) % data_len
    previous_iterator = (int(iterator) - 1) % data_len
    markup.insert(
        InlineKeyboardButton(text="⬅️", callback_data=navigation_records_cd.new(type=type, iterator=previous_iterator)))
    markup.insert(
        InlineKeyboardButton(text="➡️", callback_data=navigation_records_cd.new(type=type, iterator=next_iterator)))
    markup.insert(InlineKeyboardButton(text="Закрыть", callback_data="0"))
    return markup
