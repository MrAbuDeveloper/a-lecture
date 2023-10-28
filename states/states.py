from telebot.handler_backends import State, StatesGroup


class RegisterStates(StatesGroup):
    full_name = State()
    contact = State()
    birthdate = State()
