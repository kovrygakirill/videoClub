from ..models import Movie, Category


class MovieQuery:
    @staticmethod
    def filterHome(params):
        result = Movie.object.order_by("-created_date")

        if params.get("movies"):
            result = MovieQuery.filterCategories_detail(params)
        if params.get("sort"):
            result = MovieQuery.filterCategories_detail(params)

        return result

    @staticmethod
    def filterCategories_detail(params):
        result = Movie.object.order_by("-created_date")

        if params.get("slug"):
            result = MovieQuery.slugMovie(result, params['slug'])
        if params.get("sort"):
            result = MovieQuery.sortMovie(result, params['sort'])
        if params.get("movies"):
            result = MovieQuery.searchMovies(result, params['movies'])

        return result

    @staticmethod
    def searchMovies(scope, title):
        return scope.filter(movie_name=title)

    @staticmethod
    def sortMovie(scope, title):
        if title == 'Alphabet':
            result = scope.order_by("movie_name")
        elif title == 'Date':
            result = scope.order_by("-created_date")
        else:
            result = scope

        return result

    @staticmethod
    def slugMovie(scope, title):
        if Category.object.filter(slug=title).exists():
            category = Category.object.get(slug=title)
            return scope.filter(category=category)
        else:
            return scope
