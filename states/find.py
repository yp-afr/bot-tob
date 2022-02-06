from aiogram.dispatcher.filters.state import StatesGroup, State


class Find(StatesGroup):
    FindBy = State()
    InputText = State()
    ShowRecords = State()
