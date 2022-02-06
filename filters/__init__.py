from .admin import IsAdmin
from .not_admin import IsNotAdmin
from .text_button import TextButton


def setup(dp):
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsNotAdmin)
    dp.filters_factory.bind(TextButton)