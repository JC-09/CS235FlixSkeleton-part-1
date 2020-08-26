
import csv

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director

class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies = list()
        self.__dataset_of_actors = list()
        self.__dataset_of_directors = list()
        self.__dataset_of_genres = list()


    def read_csv_file(self):
        duplicated_genre = []
        duplicated_actors = []
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)
            for row in movie_file_reader:
                # Append to the movie data set
                title = row['Title']
                year = int(row['Year'])
                movie = Movie(title, year)
                if (movie not in self.__dataset_of_movies):
                    self.__dataset_of_movies.append(movie)
                # Store potential duplicated actors
                duplicated_actors.append(row['Actors'].split(','))  # This is a list of list

                # Store unique directors
                director = Director(row['Director'])
                if director not in self.__dataset_of_directors:
                    self.__dataset_of_directors.append(director)

                # Store potential duplicated genres
                duplicated_genre.append(row['Genre'].split(','))

        for actor_list in duplicated_actors:
            for current_actor in actor_list:
                current_actor = Actor(current_actor)
                if current_actor not in self.__dataset_of_actors:
                    self.__dataset_of_actors.append(current_actor)

        for genre_list in duplicated_genre:
            for current_genre in genre_list:
                current_genre = Genre(current_genre)
                if current_genre not in self.__dataset_of_genres:
                    self.__dataset_of_genres.append(current_genre)

    @property
    def dataset_of_movies(self):
        return self.__dataset_of_movies

    @property
    def dataset_of_actors(self):
        return self.__dataset_of_actors

    @property
    def dataset_of_directors(self):
        return self.__dataset_of_directors

    @property
    def dataset_of_genres(self):
        return self.__dataset_of_genres