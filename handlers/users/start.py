from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default import main
from loader import dp


@dp.message_handler(CommandStart(), admin_check=True, state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=await main.get_keyboard())
