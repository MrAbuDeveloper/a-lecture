from telebot.types import Message, ReplyKeyboardRemove
from data.loader import bot, db
from keyboards.default import register_button, send_contact
from states.states import RegisterStates


@bot.message_handler(func=lambda message: message.text == 'Buyurtma 🛍')
def reaction_to_order(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    check = db.check_user_info(user_id)
    if None in check:
        text = "Siz ro'yhatdan o'tmagansiz! Buyurtma berish uchun ro'yhatdan o'ting iltimos!"
        markup = register_button()
    else:
        text = "Online do'konimizga xush kelibsiz! Mahsulot tanlang 😊"
        markup = None
    bot.send_message(chat_id, text, reply_markup=markup)


# REGISTRATION PART

@bot.message_handler(func=lambda message: message.text == "Ro'yhatdan o'tish ✍️")
def reaction_to_register(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    bot.set_state(user_id, RegisterStates.full_name, chat_id)
    bot.send_message(chat_id, "I.F.Sh kiriting: ", reply_markup=ReplyKeyboardRemove())


@bot.message_handler(content_types=['text'], state=RegisterStates.full_name)
def reaction_to_name(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    with bot.retrieve_data(user_id, chat_id) as data:
        data['full_name'] = message.text.title()
    bot.set_state(user_id, RegisterStates.contact, chat_id)
    bot.send_message(chat_id, 'Kontaktingizni ulashing', reply_markup=send_contact())


@bot.message_handler(content_types=['contact'], state=RegisterStates.contact)
def reaction_to_contact(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    with bot.retrieve_data(user_id, chat_id) as data:
        data['contact'] = message.contact.phone_number
    bot.set_state(user_id, RegisterStates.birthdate, chat_id)
    bot.send_message(chat_id, "Tug'ilgan kuningizni kiriting:\nyyyy.mm.dd ko'rinishida",
                     reply_markup=ReplyKeyboardRemove())


@bot.message_handler(content_types=['text'], state=RegisterStates.birthdate)
def reaction_to_birthdate(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    with bot.retrieve_data(user_id, chat_id) as data:
        full_name = data['full_name']
        contact = data['contact']
    db.insert_user_info(full_name, contact, message.text, user_id)
    bot.set_state(user_id, RegisterStates.contact, chat_id)
    bot.send_message(chat_id, "Ro'yhatdan o'tdingiz",
                     reply_markup=ReplyKeyboardRemove())





