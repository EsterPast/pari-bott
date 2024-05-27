from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio

from aiogram.fsm.context import  FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.state import StateFilter
from state import UserStates

from config import TOKEN

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id,"Привет! Я эхо-бот.")
    await state.set_state(UserStates.BASE)

@dp.message(Command("test"),StateFilter(UserStates.BASE))
async def stat(message: types.Message):
    await bot.send_message(message.chat.id,"BASE")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())