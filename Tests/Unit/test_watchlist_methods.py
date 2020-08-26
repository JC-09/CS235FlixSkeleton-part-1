from domainmodel.watchlist import WatchList
from domainmodel.movie import Movie
import pytest

@pytest.fixture
def watchlist():
    return WatchList()

def test_init(watchlist):
    assert watchlist.size() == 0

def test_size_after_adding_movies(watchlist):
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    assert watchlist.size() == 3

def test_add_movie(watchlist):
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    assert watchlist.size() == 2
    watchlist.add_movie(Movie("Ice Age", 2002))
    assert watchlist.size() == 2

def test_remove_movies(watchlist):
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    watchlist.remove_movie(Movie("Ice Age", 2002))
    assert watchlist.size() == 2
    watchlist.remove_movie(Movie("Star War", 2017))  #remove an movie that doesn't exist in the watchlist
    assert watchlist.size() == 2

def test_select_movie_to_watch(watchlist):
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    assert repr(watchlist.select_movie_to_watch(0)) == "<Movie Moana, 2016>"
    assert watchlist.select_movie_to_watch(-1) is None
    assert watchlist.select_movie_to_watch(3) is None

def test_first_movie_in_watchlist(watchlist):
    assert watchlist.first_movie_in_watchlist() is None
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    assert repr(watchlist.first_movie_in_watchlist()) == "<Movie Moana, 2016>"

def test_iter_and_next(watchlist):
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    i = iter(watchlist)
    assert repr(next(i)) == "<Movie Moana, 2016>"
    assert repr(next(i)) == "<Movie Ice Age, 2002>"
    assert repr(next(i)) == "<Movie Guardians of the Galaxy, 2012>"
    with pytest.raises(StopIteration):
        assert repr(next(i)) == StopIteration