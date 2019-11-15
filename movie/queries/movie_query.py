from ..models import Movie


class MovieQuery:
    @staticmethod
    def result(title):
        if title == '':
            return Movie.object.order_by("-created_date")
        else:
            return Movie.object.filter(movie_name=title)
