import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from loader import dp

@dp.message_handler(Command('items'))
async def show_items(message: Message):
    await message.answer(text='For You We Have: \n'
                              'Movies And Shows. \n'
                              'For Cancel - PUSH THE TEMPO')

@dp.callback_query_handler(text_contains='movie')
async def choose_movie(call: CallbackQuery):
    await call.answer(cache_time=60)  # cashtime for saving answers
    callback_data = call.data
    logging.info(f'call = {callback_data}')