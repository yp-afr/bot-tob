from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

# from affichebot.utils.db_api.commands import get_admins
from data.config import ADMINS
from utils.api import Api


class IsAdmin(BoundFilter):
    key = "admin_check"

    def __init__(self, admin_check):
        self.admin_check = admin_check

    async def check(self, message: types.Message) -> bool:
        # list_admins = await get_admins()
        list_admins = ADMINS
        uid = str(message.from_user.id)
        data = {
            "action": "Auth::authUser",
            "string": uid
        }
        response = await Api.sendRequestApi(data)
        if response or uid in list_admins:
            return True
        else:
            return False
