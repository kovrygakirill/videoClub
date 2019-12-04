import django
django.setup()

from unittest import TestCase
from movie.queries.pagination import Paginat
from movie.models import Movie


class TestPaginat(TestCase):
    def test_getPaginator_getMoviesPage1AndCorrectListMovies_firstPageMovies(self):
        movies_list = Movie.object.order_by("-created_date")
        page = 1
        movies = Paginat.getPaginator(movies_list, page)

        result = Movie.object.order_by("-created_date")[:6]
        self.assertEquals(list(movies), list(result))

    def test_getPaginator_getMoviesWrongPageIntegerAndCorrectListMovies_endPageMovies(self):
        movies_list = Movie.object.order_by("-created_date")
        page = 105
        movies = Paginat.getPaginator(movies_list, page)

        countMoviesEndPage = len(Movie.object.all()) - len(Movie.object.all()) % 6
        result = Movie.object.order_by("-created_date")[countMoviesEndPage:]
        self.assertEquals(list(movies), list(result))

    def test_getPaginator_getMoviesWrongPageAndCorrectListMovies_firstPageMovies(self):
        movies_list = Movie.object.order_by("-created_date")
        page = "fdbdf"
        movies = Paginat.getPaginator(movies_list, page)

        result = Movie.object.order_by("-created_date")[:6]
        self.assertEquals(list(movies), list(result))

    def test_getPaginator_getMoviesEmptyPageAndCorrectListMovies_FirstPageMovies(self):
        movies_list = Movie.object.order_by("-created_date")
        page = ""
        movies = Paginat.getPaginator(movies_list, page)

        result = Movie.object.order_by("-created_date")[:6]
        self.assertEquals(list(movies), list(result))

    def test_getPaginator_getMoviesNullPageAndCorrectListMovies_FirstPageMovies(self):
        movies_list = Movie.object.order_by("-created_date")
        page = None
        movies = Paginat.getPaginator(movies_list, page)

        result = Movie.object.order_by("-created_date")[:6]
        self.assertEquals(list(movies), list(result))

    def test_getPaginator_getMoviesNoneListMovies_firstPageMovies(self):
        movies_list = None
        page = 1
        movies = Paginat.getPaginator(movies_list, page)

        result = None
        self.assertEquals(movies, result)

    def test_getPaginator_getMoviesEmptyListMovies_firstPageMovies(self):
        movies_list = []
        page = 1
        movies = Paginat.getPaginator(movies_list, page)

        result = None
        self.assertEquals(movies, result)
