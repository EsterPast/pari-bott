from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton


def  get_keyboard(buttons):
    kb = []
    for buttons in buttons:
        kb.append([KeyboardButton(text=buttons)])
    reply_makeup = ReplyKeyboardMarkup(keyboard=kb,resize_keyboard=True)
    return reply_makeup