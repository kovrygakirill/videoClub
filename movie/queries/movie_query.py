from ..models import Movie, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class MovieQuery:
    @staticmethod
    def filterRequest(params):
        result = Movie.object.order_by("-created_date")

        if params:
            if params.get("sort"):
                result = MovieQuery.sortMovie(result, params['sort'])
            if params.get("search"):
                result = MovieQuery.searchMovies(result, params['search'])
            if params.get("pk"):
                result = MovieQuery.pkMovie(result, params['pk'])
            if params.get("slug"):
                result = MovieQuery.slugMovie(result, params['slug'])

        return result

    @staticmethod
    def sortMovie(scope, sort):
        if scope:
            if sort == 'Alphabet':
                result = scope.order_by("movie_name")
            elif sort == 'Date':
                result = scope.order_by("-created_date")
            else:
                result = scope

            return result
        else:
            return []

    @staticmethod
    def searchMovies(scope, search):
        if scope:
            return scope.filter(movie_name=search)
        else:
            return []

    @staticmethod
    def pkMovie(scope, pk):
        if Movie.object.filter(pk=pk).exists() and scope:
            return scope.get(pk=pk)
        else:
            return []

    @staticmethod
    def slugMovie(scope, slug):
        if Category.object.filter(slug=slug).exists() and scope:
            category = Category.object.get(slug=slug)
            return scope.filter(category=category)
        else:
            return []

    @staticmethod
    def getPaginator(movie_list, page):
        show_movies_page = 6
        paginator = Paginator(movie_list, show_movies_page)

        try:
            movies = paginator.page(page)
        except PageNotAnInteger:
            movies = paginator.page(1)
        except EmptyPage:
            movies = paginator.page(paginator.num_pages)

        return movies


