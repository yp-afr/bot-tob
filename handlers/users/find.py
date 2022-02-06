import logging
import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from filters.text_button import TextButton
from keyboards.default import find, main, cancel
from keyboards.inline import show_records, navigate_records
from keyboards.inline.navigate_records import navigation_records_cd
from keyboards.inline.show_records import show_records_cd
from loader import dp
from states.find import Find
from utils.api import Api
from utils.misc import generate_record_text
from utils.misc.record import convertDate


@dp.message_handler(TextButton("go_back"), admin_check=True, state=Find.FindBy)
async def go_back(message: types.Message, state: FSMContext):
    await message.answer("Меню: ", reply_markup=await main.get_keyboard())
    await state.reset_state()


@dp.message_handler(TextButton("find"), admin_check=True)
async def find_by(message: types.Message):
    await message.answer(f"Методы поиска: ", reply_markup=await find.get_keyboard())
    await Find.FindBy.set()


@dp.message_handler(TextButton("by_name"), admin_check=True, state=Find.FindBy)
async def find_by_name(message: types.Message):
    await message.answer("Введите ФИО / ИНН / Номер телефона: ", reply_markup=await cancel.get_keyboard())
    await Find.InputText.set()


@dp.message_handler(TextButton("cancel"), admin_check=True, state=Find.InputText)
async def cancel_input(message: types.Message, state: FSMContext):
    await state.reset_state()
    await find_by(message)


@dp.message_handler(admin_check=True, state=Find.InputText)
async def api_find(message: types.Message, state: FSMContext):
    await message.answer("Выполняю поиск... 🧐")
    await search(message, state)


async def search(message: types.Message, state: FSMContext):
    data = {
        "action": "Persons::searchPersonByString",
        "string": message.text
    }
    try:
        response = await Api.sendRequestApi(data)
        print(response)
        answer_text = ''
        for values in response.get("privatbank"):
            answer_text += "<b>" + values['fullName'] + "</b>\n"
            answer_text += "ИНН: " + values['ipn'] + "\n"
            answer_text += convertDate(values['birthday']) + "\n"
            answer_text += "/show_" + values['id'] + "\n\n"

        await message.answer(answer_text, reply_markup=await find.get_keyboard())
        await Find.FindBy.set()
    except Exception as ex:
        await message.answer("Ошибка ❌")
        logging.error(ex)


@dp.message_handler(content_types=types.ContentType.TEXT, admin_check=True, state="*")
async def show_info(message: types.Message, state: FSMContext):
    if message.text.find("/show_") != -1:
        uid = message.text.split("_")[1]
        data = {
            "action": "Persons::showById",
            "uid": uid
        }
        try:
            response = await Api.sendRequestApi(data)
            data = response['answer']
            if data:
                text = await generate_record_text(data)
                await message.answer(text)
            else:
                raise ValueError("Empty array")
        except Exception as ex:
            await message.answer("Ошибка ❌")
            logging.error(ex)
