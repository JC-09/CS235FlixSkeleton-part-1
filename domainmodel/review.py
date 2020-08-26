from domainmodel.movie import Movie
from datetime import datetime
from domainmodel.user import User



class Review:
    def __init__(self, author : User, movie:Movie, review_text : str, rating : int):
        self.__author = author
        self.__movie = movie
        self.__review_text = review_text
        self.__rating = None
        self.__timestamp = datetime.today()
        if type(rating) is int:
            if 0 < rating <= 10:
                self.__rating = rating

    @property
    def author(self):
        return self.__author

    @property
    def movie(self) -> Movie:
        return self.__movie

    @property
    def review_text(self) -> str:
        return self.__review_text
    @property
    def rating(self):
        return self.__rating
    @property
    def timestamp(self):
        return self.__timestamp

    def __repr__(self):
        return "<Review for movie: {}, made by: {}, on: >".format(self.movie, self.author,self.timestamp)

    def __eq__(self, other):
        if self.movie == other.movie and self.review_text == other.review_text \
            and self.rating == other.rating and self.timestamp == other.timestamp:
            return True
        return False

    def hash(self):
        return hash((self.movie, self.timestamp))