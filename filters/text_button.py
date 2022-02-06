from aiogram import types
from aiogram.dispatcher.filters import Filter

from data.config import BUTTONS


class TextButton(Filter):
    key = "text_button"

    def __init__(self, button_code: str):
        self.button_code: str = button_code

    async def check(self, message: types.Message) -> bool:
        try:
            name = BUTTONS.get(self.button_code)
            return message.text == name
        except Exception as ex:
            return False
