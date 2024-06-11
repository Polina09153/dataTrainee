import requests
import pandas as pd
from collections import Counter

OMDB_API_KEY = '8382c80f'


def get_movie_data(title):
    url = f'http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}'
    response = requests.get(url)
    return response.json()


movie_titles = ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Inception', 'Forrest Gump']
movie_data = [get_movie_data(title) for title in movie_titles]
movies_df = pd.DataFrame(movie_data)



most_popular_movies = movies_df.sort_values('imdbRating', ascending=False)
print('Самые популярные фильмы:')
print(most_popular_movies[['Title', 'imdbRating']])


movie_genres = [genre.split(', ') for genre in movies_df['Genre']]
genre_counts = Counter([genre for genres in movie_genres for genre in genres])
print('\nСамые популярные жанры:')
print(genre_counts.most_common(10))

