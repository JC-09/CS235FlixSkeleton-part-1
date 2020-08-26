from domainmodel.movie import Movie
from activitysimulations.watchingsimulation import MovieWatchingSimulation
import pytest

@pytest.fixture
def star_warWatchSimulation():
    return MovieWatchingSimulation(Movie("Star War", 2018))




