from aiogram.dispatcher.filters.state import StatesGroup, State


class UserSettings(StatesGroup):
    ChooseOne = State()
    AddUser = State()