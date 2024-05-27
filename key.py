from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from state import UserStates


def  get_keyboard(buttons):
    kb = []
    for buttons in buttons:
        kb.append([KeyboardButton(text=buttons)])
    reply_makeup = ReplyKeyboardMarkup(keyboard=kb,resize_keyboard=True)
    return reply_makeup

keyboards = {
    UserStates.BASE: get_keyboard(["Мои пари","Создать пари"]),
    UserStates.CREATING_PARI: get_keyboard(["Отмена"])
}