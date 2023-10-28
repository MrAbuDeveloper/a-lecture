from telebot.types import Message
from data.loader import bot, db
from keyboards.default import main_menu_default


@bot.message_handler(commands=['start'], chat_types='private')
def start(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    db.insert_telegram_id_users(user_id)
    bot.send_message(chat_id=chat_id, text=f'Salom, {message.from_user.first_name}!',
                     reply_markup=main_menu_default())

