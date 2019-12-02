from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Paginat:
    @staticmethod
    def getPaginator(movie_list, page):
        if movie_list:
            show_movies_page = 6
            paginator = Paginator(movie_list, show_movies_page)

            try:
                movies = paginator.page(page)
            except PageNotAnInteger:
                movies = paginator.page(1)
            except EmptyPage:
                movies = paginator.page(paginator.num_pages)

            return movies
        else:
            return None
