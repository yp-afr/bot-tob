from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
API_URL = env.str("API_URL")
API_TOKEN = env.str("API_TOKEN")

BUTTONS = {
    "find": "🔍 Поиск",
    "settings": "⚙️ Настройки",
    "go_back": "◀️ Назад",
    "by_name": "🙎‍♂️ ФИО / 📞 Телефон / 📄 ИНН",
    "by_number": "📞 Телефон",
    "by_car": "🚗 Автомобиль",
    "add_user": "👨 Добавить пользователя",
    "cancel": "🚫 Отмена"
}
