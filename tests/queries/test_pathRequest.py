import django
django.setup()

from unittest import TestCase
from movie.queries.path_request import PathRequest


class TestPathRequest(TestCase):
    def test_getQueryWithoutPage_getPathEmptyRequest_EmptyPath(self):
        request = ''
        path = PathRequest.getQueryWithoutPage(request)

        result = ''
        self.assertEquals(path, result)

    def test_getQueryWithoutPage_getPathNoneRequest_EmptyPath(self):
        request = None
        path = PathRequest.getQueryWithoutPage(request)

        result = ''
        self.assertEquals(path, result)

    def test_getQueryWithoutPage_getPathRequestSort_EmptyPath(self):
        request = "sort=Alphabet"
        path = PathRequest.getQueryWithoutPage(request)

        result = "sort=Alphabet&"
        self.assertEquals(path, result)

    def test_getQueryWithoutPage_getPathRequestSortAndPage_EmptyPath(self):
        request = "sort=Alphabet&page=1"
        path = PathRequest.getQueryWithoutPage(request)

        result = "sort=Alphabet&"
        self.assertEquals(path, result)

    def test_getQueryWithoutPage_getPathRequestPage_EmptyPath(self):
        request = "page=1"
        path = PathRequest.getQueryWithoutPage(request)

        result = ""
        self.assertEquals(path, result)
