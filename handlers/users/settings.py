import logging

from aiogram import types
from aiogram.dispatcher import FSMContext

from filters import TextButton
from keyboards.default import user_settings, cancel, main
from loader import dp
from states.user_settings import UserSettings
from utils.api import Api


@dp.message_handler(TextButton("settings"), admin_check=True)
async def settings(message: types.Message):
    await message.answer("Настройки: ", reply_markup=await user_settings.get_keyboard())
    await UserSettings.ChooseOne.set()


@dp.message_handler(TextButton("go_back"), state=UserSettings.ChooseOne, admin_check=True)
async def go_back_from_setting(message: types.Message, state: FSMContext):
    await message.answer("Меню: ", reply_markup=await main.get_keyboard())
    await state.reset_state()


@dp.message_handler(TextButton("add_user"), state=UserSettings.ChooseOne, admin_check=True)
async def add_user(message: types.Message):
    await message.answer("Отправьте контакт пользователя которому хотите открыть доступ",
                         reply_markup=await cancel.get_keyboard())
    await UserSettings.AddUser.set()


@dp.message_handler(TextButton("cancel"), state=UserSettings.AddUser, admin_check=True)
async def cancel_adding_user(message: types.Message, state: FSMContext):
    await state.reset_state()
    await settings(message)


@dp.message_handler(content_types=types.ContentType.CONTACT, state=UserSettings.AddUser, admin_check=True)
async def get_contact(message: types.Message):
    print("text")
    data = {
        "action": "Auth::createUser",
        "phone": message.contact.phone_number,
        "name": message.contact.first_name,
        "uid": message.contact.user_id
    }
    try:
        response = await Api.sendRequestApi(data)
        await settings(message)


    except Exception as ex:
        await message.answer("Ошибка ❌")
        logging.error(ex)
