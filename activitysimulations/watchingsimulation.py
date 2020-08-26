from domainmodel.movie import Movie
from domainmodel.review import Review
from domainmodel.user import User


class MovieWatchingSimulation:
    def __init__(self, movie:Movie):
        self.__movie = None
        if isinstance(movie, Movie):
            self.__movie = movie
            self.__users = list()     # A list of user watching the movie
            self.__reviews = list()   # A list of reviews (movie) made by this set of user for this particular movie

    @property
    def movie(self):
        return self.__movie

    @property
    def users(self):
        return self.__users

    @property
    def reviews(self):
        return self.__reviews


    def add_user(self, user:User):
        if isinstance(user, User):
            self.__users.append(user)
            user.watched_movies.append(self.movie)

    def add_review(self, review : Review):  #Currently only supports one review per user per movie
        if isinstance(review, Review) and review.movie == self.movie and review.author in self.__users: #only allow users who have viewed this
            # movie to write review for this movie
            self.__reviews.append(review)

    def __repr__(self):
        print("Movie Watching Simulation - {}".format(self.movie.title))



