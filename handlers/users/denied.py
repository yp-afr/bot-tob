from aiogram import types

from loader import dp


@dp.message_handler(not_admin_check=True)
async def access_denied(message: types.Message):
    await message.answer("Доступ отклонён 🙅‍♂️")
