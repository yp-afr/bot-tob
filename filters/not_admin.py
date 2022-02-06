from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from data.config import ADMINS
from utils.api import Api


class IsNotAdmin(BoundFilter):
    key = "not_admin_check"

    def __init__(self, not_admin_check):
        self.not_admin_check = not_admin_check

    async def check(self, message: types.Message) -> bool:
        # list_admins = await get_admins()
        list_admins = ADMINS
        uid = str(message.from_user.id)
        data = {
            "action": "Auth::authUser",
            "string": uid
        }
        response = await Api.sendRequestApi(data)
        if not response and uid not in list_admins:
            return True
        else:
            return False
