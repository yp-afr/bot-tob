import logging

from aiogram import Dispatcher

from data.config import ADMINS
from keyboards.default import main


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Бот Запущен", reply_markup=await main.get_keyboard(),
                                      disable_notification=True)
        except Exception as err:
            logging.exception(err)
