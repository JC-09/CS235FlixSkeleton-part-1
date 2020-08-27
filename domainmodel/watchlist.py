from domainmodel.movie import Movie

class WatchList:
    def __init__(self):
        self.__watchlist = list()
        self.__start_index = 0

    @property
    def watchlist(self):
        return self.__watchlist
    def add_movie(self, movie : Movie):
        if isinstance(movie, Movie):
            if movie not in self.__watchlist:
                self.__watchlist.append(movie)

    def remove_movie(self, movie : Movie):
        try:
            self.__watchlist.remove(movie)
        except ValueError:
            return False

    def select_movie_to_watch(self, index:int):
        if index < 0:
            return None
        try:
            return self.__watchlist[index]
        except IndexError:
            return None

    def size(self):
        return len(self.__watchlist)

    def first_movie_in_watchlist(self):
        movie = None
        if self.size() > 0:
            movie = self.__watchlist[0]
        return movie

    def __iter__(self):
        return iter(self.__watchlist)

    def __next__(self):
        try:
            to_return = self.self.__watchlist[self.__start_index]
            self.__start_index += 1
            return to_return
        except IndexError:
            raise StopIteration

