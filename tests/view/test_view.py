#!/usr/bin/env python
# -*- coding: utf8 -*-

import django

django.setup()

from django.core.paginator import Paginator
from django.shortcuts import render
from django.test import RequestFactory

from unittest import TestCase

from movie.models import Movie, Category
from movie.views import detail_category, detail_movies, post_Home


class TestView(TestCase):
    def test_detail_category_GetTemplateWrongSlug_TemplateForError(self):
        request = RequestFactory().get("/category/dramaa/")
        slug = "dramaa"
        expect = detail_category(request, slug)

        result = render(request, 'request_not_found.html')
        self.assertEquals(expect.tell(), result.tell())

    def test_detail_category_GetTemplateCorrectSlug_CorrectTemplate(self):
        request = RequestFactory().get("/category/drama/")
        slug = "drama"
        path = ''

        movies_list = Movie.object.order_by("-created_date").filter(category=Category.object.get(slug=slug))
        movies = Paginator(movies_list, 6)
        movies = movies.page(1)
        rangePage = range(1, 2)

        expect = detail_category(request, slug)

        result = render(request, "categories_detail.html",
                        {'movies': movies, 'slug': slug, 'path': path, 'rangePage': rangePage})
        self.assertEquals(expect.tell(), result.tell())

    def test_detail_movies_GetTemplateWrongPk_TemplateForError(self):
        request = RequestFactory().get("/movie/10000")
        pk = 10000
        movies = []

        expect = detail_movies(request, pk)

        result = render(request, "request_not_found.html")
        self.assertEquals(expect.tell(), result.tell())

    def test_detail_movies_GetTemplateCorrectPk_CorrectTemplate(self):
        request = RequestFactory().get("/movie/1")
        pk = 1
        movie = Movie.object.get(pk=pk)

        expect = detail_movies(request, pk)

        result = render(request, 'movie.html', {'movie': movie})
        self.assertEquals(expect.tell(), result.tell())

    def test_post_Home_GetTemplateWrongSearch_TemplateForError(self):
        request = RequestFactory().get("/?search=sdsdvs")
        expect = post_Home(request)

        result = render(request, 'request_not_found.html')
        self.assertEquals(expect.tell(), result.tell())

    def test_post_Home_GetTemplateCorrectSearch_CorrectTemplate(self):
        request = RequestFactory().get("/?search=Аст")
        path = 'search=%D0%90%D1%81%D1%82&'
        categories = Category.object.all()
        movies_list = Movie.object.filter(movie_name__iregex='Аст')
        movies = Paginator(movies_list, 6)
        movies = movies.page(1)
        rangePage = range(1, 2)

        expect = post_Home(request)

        result = render(request, 'home.html',
                        {'movies': movies, 'categories': categories, 'path': path, 'rangePage': rangePage})
        self.assertEquals(expect.tell(), result.tell())
