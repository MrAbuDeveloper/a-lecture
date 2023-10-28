from telebot import TeleBot, custom_filters
from database.database import DataBase
from .config import TOKEN
from telebot.storage import StateMemoryStorage

bot = TeleBot(TOKEN, state_storage=StateMemoryStorage(), use_class_middlewares=True)

db = DataBase()

bot.add_custom_filter(custom_filters.StateFilter(bot))

