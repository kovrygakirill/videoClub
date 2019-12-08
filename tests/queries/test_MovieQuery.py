#!/usr/bin/env python
# -*- coding: utf8 -*-

import django
django.setup()

# from django.test import TestCase
import unittest
from movie.queries.movie_query import MovieQuery
from movie.models import Movie, Category
# from ..movie.queries.movie_query import MovieQuery
# from movie.queries.movie_query import MovieQuery
# from movie.models import Movie, Category


class TestMovieQuery(unittest.TestCase):
    def test_filterRequest_getMoviesEmptyParams_AllMoviesDate(self):
        # from queries.movie_query import MovieQuery
        # from models import Category,Movie
        params = {}
        movies = MovieQuery.filterRequest(params)

        result = Movie.object.order_by("-created_date")
        self.assertEquals(list(movies), list(result))

    def test_filterRequest_getMoviesPK1_MoviesCorrect(self):
        params = {'pk': 1}
        movies = MovieQuery.filterRequest(params)

        result = Movie.object.all().get(pk=1)
        self.assertEquals(movies, result)

    def test_filterRequest_getMoviesCorrectSlugAndSort_MoviesKomediyaOnAlphabet(self):
        params = {'slug': 'komediya', 'sort': 'Alphabet'}
        movies = MovieQuery.filterRequest(params)

        result = Movie.object.filter(category=Category.object.get(slug='komediya')).order_by("movie_name")
        self.assertEquals(list(movies), list(result))

    def test_filterRequest_getMoviesCorrectSlug_MoviesDrama(self):
        params = {'slug': 'drama'}
        movies = MovieQuery.filterRequest(params)

        result = Movie.object.order_by("-created_date").filter(category=Category.object.get(slug='drama'))
        self.assertEquals(list(movies), list(result))

    def test_filterRequest_getMoviesCorrectSearch_MovieCorrect(self):
        params = {'search': "Почему он?"}
        movie = MovieQuery.filterRequest(params)

        result = Movie.object.filter(movie_name='Почему он?')
        self.assertEquals(list(movie), list(result))

    def test_filterRequest_getMoviesNoneParams_AllMoviesDate(self):
        params = None
        movie = MovieQuery.filterRequest(params)

        result = Movie.object.order_by("-created_date")
        self.assertEquals(list(movie), list(result))

    def test_filterRequest_getMoviesWrongPK_MoviesNotExists(self):
        params = {'pk': 1123}
        movies = MovieQuery.filterRequest(params)

        result = []
        self.assertEquals(movies, result)

    def test_filterRequest_getMoviesWrongSlug_MoviesNotExists(self):
        params = {'slug': 'tiller'}
        movies = MovieQuery.filterRequest(params)

        result = []
        self.assertEquals(movies, result)

    def test_filterRequest_getMoviesWrongSearch_MoviesNotExists(self):
        params = {'search': 'kirill'}
        movies = MovieQuery.filterRequest(params)

        result = []
        self.assertEquals(list(movies), result)

    def test_filterRequest_getMoviesWrongSort_AllMoviesDate(self):
        params = {'sort': 'image'}
        movies = MovieQuery.filterRequest(params)

        result = Movie.object.order_by("-created_date")
        self.assertEquals(list(movies), list(result))

    def test_filterRequest_getMoviesCorrectSlugAndWrongSort_MoviesKomediyaOnDate(self):
        params = {'slug': 'komediya', 'sort': 'image'}
        movies = MovieQuery.filterRequest(params)

        result = Movie.object.filter(category=Category.object.get(slug='komediya')).order_by("-created_date")
        self.assertEquals(list(movies), list(result))

    def test_filterRequest_getMoviesWrongSlugAndCorrectSort_MoviesNotExists(self):
        params = {'slug': 'tiller', 'sort': 'Alphabet'}
        movies = MovieQuery.filterRequest(params)

        result = []
        self.assertEquals(list(movies), list(result))

    def test_filterRequest_getMoviesNoneSlugAndCorrectSort_AllMoviesSort(self):
        params = {'slug': None, 'sort': 'Alphabet'}
        movies = MovieQuery.filterRequest(params)

        result = Movie.object.order_by("movie_name")
        self.assertEquals(list(movies), list(result))

    def test_filterRequest_getMoviesCorrectSlugAndNoneSort_Moviesslug(self):
        params = {'slug': 'drama', 'sort': None}
        movies = MovieQuery.filterRequest(params)

        result = Movie.object.filter(category=Category.object.get(slug='drama')).order_by("-created_date")
        self.assertEquals(list(movies), list(result))

    def test_filterRequest_getMoviesWrongSlugAndSort_MoviesNotExists(self):
        params = {'slug': 'tiller', 'sort': 'image'}
        movies = MovieQuery.filterRequest(params)

        result = []
        self.assertEquals(list(movies), list(result))

    def test_filterRequest_getMoviesWrongSearchAndSort_MoviesNotExists(self):
        params = {'search': 'kyky', 'sort': 'image'}
        movies = MovieQuery.filterRequest(params)

        result = []
        self.assertEquals(list(movies), list(result))

    def test_filterRequest_getMoviesWrongSearchAndCorrectSort_MoviesNotExists(self):
        params = {'search': 'kyky', 'sort': 'Alphabet'}
        movies = MovieQuery.filterRequest(params)

        result = []
        self.assertEquals(list(movies), list(result))

    def test_filterRequest_getMoviesCorrectSearchAndWrongSort_MoviesCorrect(self):
        params = {'search': "Почему он?", 'sort': 'lol'}
        movies = MovieQuery.filterRequest(params)

        result = Movie.object.filter(movie_name='Почему он?').order_by("-created_date")
        self.assertEquals(list(movies), list(result))

    def test_filterRequest_getMoviesCorrectSearchAndSort_MoviesCorrect(self):
        params = {'search': "Почему он?", 'sort': 'Alphabet'}
        movies = MovieQuery.filterRequest(params)

        result = Movie.object.filter(movie_name='Почему он?').order_by("movie_name")
        self.assertEquals(list(movies), list(result))

    def test_slugMovie_getMoviesCorrectSlug_MoviesKomediya(self):
        scope = Movie.object.order_by("-created_date")
        slug = 'komediya'
        movies = MovieQuery.slugMovie(scope, slug)

        result = Movie.object.order_by("-created_date").filter(category=Category.object.get(slug=slug))
        self.assertEquals(list(movies), list(result))

    def test_slugMovie_getMoviesWrongSlug_MoviesNotExists(self):
        scope = Movie.object.order_by("-created_date")
        slug = 'tiller'
        movies = MovieQuery.slugMovie(scope, slug)

        result = []
        self.assertEquals(list(movies), list(result))

    def test_slugMovie_getMoviesNoneSlug_MoviesNotExists(self):
        scope = Movie.object.order_by("-created_date")
        slug = None
        movies = MovieQuery.slugMovie(scope, slug)

        result = []
        self.assertEquals(list(movies), list(result))

    def test_slugMovie_getMoviesEmptySlug_MoviesNotExists(self):
        scope = Movie.object.order_by("-created_date")
        slug = ''
        movies = MovieQuery.slugMovie(scope, slug)

        result = []
        self.assertEquals(list(movies), list(result))

    def test_slugMovie_getMoviesNoneScope_MoviesNotExists(self):
        scope = None
        slug = 'komediya'
        movies = MovieQuery.slugMovie(scope, slug)

        result = []
        self.assertEquals(list(movies), list(result))

    def test_sortMovie_getMoviesCorrectSort_MoviesAlphabet(self):
        scope = Movie.object.order_by("-created_date")
        sort = 'Alphabet'
        movies = MovieQuery.sortMovie(scope, sort)

        result = Movie.object.order_by('movie_name')
        self.assertEquals(list(movies), list(result))

    def test_sortMovie_getMoviesCorrectSort_MoviesDate(self):
        scope = Movie.object.order_by("-created_date")
        sort = 'Date'
        movies = MovieQuery.sortMovie(scope, sort)

        result = Movie.object.order_by("-created_date")
        self.assertEquals(list(movies), list(result))

    def test_sortMovie_getMoviesEmptySort_MoviesDate(self):
        scope = Movie.object.order_by("-created_date")
        sort = ''
        movies = MovieQuery.sortMovie(scope, sort)

        result = Movie.object.order_by("-created_date")
        self.assertEquals(list(movies), list(result))

    def test_sortMovie_getMoviesNoneSort_MoviesNotExists(self):
        scope = Movie.object.order_by("-created_date")
        sort = None
        movies = MovieQuery.sortMovie(scope, sort)

        result = Movie.object.order_by("-created_date")
        self.assertEquals(list(movies), list(result))

    def test_sortMovie_getMoviesWrongSort_MoviesDate(self):
        scope = Movie.object.order_by("-created_date")
        sort = "image"
        movies = MovieQuery.sortMovie(scope, sort)

        result = Movie.object.order_by("-created_date")
        self.assertEquals(list(movies), list(result))

    def test_sortMovie_getMoviesNoneScope_MoviesDate(self):
        scope = None
        sort = "image"
        movies = MovieQuery.sortMovie(scope, sort)

        result = []
        self.assertEquals(list(movies), list(result))

    def test_searchMovies_getMovieCorrectSearch_MovieCorrect(self):
        scope = Movie.object.order_by("-created_date")
        search = 'Почему он?'
        movies = MovieQuery.searchMovies(scope, search)

        result = Movie.object.filter(movie_name='Почему он?')
        self.assertEquals(list(movies), list(result))

    def test_searchMovies_getMovieWrongSearch_MoviesNotExists(self):
        scope = Movie.object.order_by("-created_date")
        search = 'Почему'
        movies = MovieQuery.searchMovies(scope, search)

        result = Movie.object.filter(movie_name='Почему он?')
        self.assertEquals(list(movies), list(result))

    def test_searchMovies_getMovieNoneSearch_MoviesNotExists(self):
        scope = Movie.object.order_by("-created_date")
        search = None
        movies = MovieQuery.searchMovies(scope, search)

        result = []
        self.assertEquals(list(movies), list(result))

    def test_searchMovies_getMovieNoneScope_MoviesNotExists(self):
        scope = None
        search = 'Почему'
        movies = MovieQuery.searchMovies(scope, search)

        result = []
        self.assertEquals(list(movies), list(result))

    def test_pkMovie_getMovieCorrectPK_MovieCorrect(self):
        scope = Movie.object.order_by("-created_date")
        pk = 1
        movies = MovieQuery.pkMovie(scope, pk)

        result = Movie.object.get(pk=1)
        self.assertEquals(movies, result)

    def test_pkMovie_getMovieWrongPK_MoviesNotExists(self):
        scope = Movie.object.order_by("-created_date")
        pk = 1102
        movies = MovieQuery.pkMovie(scope, pk)

        result = []
        self.assertEquals(movies, result)

    def test_pkMovie_getMovieNonePK_MoviesNotExists(self):
        scope = Movie.object.order_by("-created_date")
        pk = None
        movies = MovieQuery.pkMovie(scope, pk)

        result = []
        self.assertEquals(movies, result)

    def test_pkMovie_getMovieNoneScope_MoviesNotExists(self):
        scope = None
        pk = 1
        movies = MovieQuery.pkMovie(scope, pk)

        result = []
        self.assertEquals(movies, result)
