from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
storage = MemoryStorage()

#  5098772001:AAFd4zTQxb-Bew6SCs0f7B5yTiNp_Hekwg8

TOKEN = "5485477872:AAGl-JwgBpuZtefwEMBoSFs73BWYzzzOXhA"

bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot, storage=storage)
