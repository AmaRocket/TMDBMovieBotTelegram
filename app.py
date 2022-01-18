from logging import shutdown

from loader import bot


# async def on_startup(dp):
#     await bot.send_message()

async def on_shutdown(dp):
    await bot.close()



if __name__ == '__main__':
    print('It is Work!')
    from aiogram import executor
    from handlers import dp
    executor.start_polling(dp, skip_updates=True, on_shutdown=on_shutdown)





'''

PREVIOUS VERSION OF BOT


import logging

import requests
from aiogram import Bot, Dispatcher, executor, types
from config import token, api_key

import keyboards as kb

logging.basicConfig(level=logging.INFO)

TOKEN = token

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



# echo function
# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.reply(message.text)



# @dp.message_handler(commands=['search_by_year_genre'])
# async def serch_movie_by_year_genre(message: types.Message):
#     await bot.send_message(message.from_user.id, 'Enter Year And Genre Of Movies', reply_markup=kb.markup1)


@dp.message_handler()
async def get_movie_by_year_genre(message: types.Message):
    try:
        genre = 'Action'
        api_version = 3
        api_base_url = f'https://api.themoviedb.org/{api_version}'
        endpoint_path = f'/discover/movie'
        endpoint = f'{api_base_url}{endpoint_path}?api_key={api_key}&sort_by=popularity.desc&include_video=true&primary_release_year={message.text}&page=1&with_genres={genre}'
        # print(endpoint)
        # print('---------------------------------------------------------------------------------------')
        r = requests.get(endpoint)
        data = r.json()
        # pprint.pprint(data)

        for info in data['results']:
            id = info['id']
            genre_ids = info['genre_ids']
            original_name = info['original_title']
            original_language = info['original_language']
            overview = info['overview']
            vote_average = info['vote_average']
            vote_count = info['vote_count']
            release_date = info['release_date']
            popularity = info['popularity']
            poster_path = info['poster_path']
            await message.reply(
                f' Movie: {original_name}\n release date: {release_date}\n movie_id: {id}\n genre id: {genre_ids}'
                f'\n original languare {original_language}\n '
                f'overwiew: {overview}\n voteaverage: {vote_average}\n vote count: {vote_count}\n '
                f' popularity: {popularity}\n poster path: https://www.themoviedb.org/t/p/original{poster_path}\n'
                f'------------------------------------------------------------------------------------------')
    except :
        await message.reply('\U00002620 Check Your Enter! \U00002620')


if __name__ == '__main__':
    executor.start_polling(dp)
'''
