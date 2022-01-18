from tmdbv3api import TMDb, Discover, Genre
from tmdbv3api import Movie
from config import api_key




# Popular Movies List
def popular_movie():
    tmdb = TMDb()
    tmdb.api_key = api_key

    tmdb.language = 'en'
    tmdb.debug = True
    movie = Movie()

    popular = movie.popular()
    popular_list = []
    for p in popular:
        popular_list.append(p)
    return(popular_list)

# print(popular_movie())


# Search for movies by title
def find_by_name(name):
    tmdb = TMDb()
    tmdb.api_key = api_key

    tmdb.language = 'en'
    tmdb.debug = True

    movie = Movie()
    search = movie.search(f'{name}')
    movie_list = []
    for res in search:
        movie_list.append(res)
    return movie_list

# print(find_by_name("name"))




# # Recomendation by your Movie
# recommendations = movie.recommendations(movie_id=524434)
# for recommendation in recommendations:
#     print(recommendation.id)
#     print(recommendation.title)
#     print(recommendation.overview)
#     # print(recommendation.genres)
#     print('===============================================')
#



# tmdb = TMDb()
# tmdb.api_key = api_key
#
# tmdb.language = 'en'
# tmdb.debug = True
# movie = Movie()
# discover = Discover()
# movie = discover.discover_movies({
#     'year': '2000',
#     'with_genres': 28,
#     'sort_by': 'popularity.desc',
#     'vote_average.gte': 8,
#     'vote_count': 50
#
# })
#
# pic_url = 'https://www.themoviedb.org/t/p/original'
# #
# # print(movie[0]['original_language'], 'https://image.tmdb.org/t/p/original' + movie[0]['backdrop_path'])
# # print('==============================================================================================')
# # print(movie[1])
# # print(movie[-1])
#
# for res in movie:
#     try:
#         print(res.id)
#         print(res.title)
#         print(res.overview)
#         print(pic_url + res.poster_path)
#         print(res.vote_average)
#         print('===========================================')
#     except TypeError as type:
#         print('HAS NO PIC')