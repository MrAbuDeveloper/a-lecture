from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu_default():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    order = KeyboardButton('Buyurtma 🛍')
    card = KeyboardButton('Savat 🛒')
    settings = KeyboardButton('Sozlamalar ⚙️')
    feed_back = KeyboardButton('Aloqa 📥')
    markup.add(order, card, feed_back, settings)
    return markup


def register_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn = KeyboardButton("Ro'yhatdan o'tish ✍️")
    markup.add(btn)
    return markup


def send_contact():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn = KeyboardButton("Kontakt ulashish", request_contact=True)
    markup.add(btn)
    return markup

