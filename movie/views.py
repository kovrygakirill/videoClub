from django.shortcuts import render, redirect

# from django.views.generic import TemplateView
# from django.views.generic.list import ListView
# from .models import Category, Movie
# from django.views.generic.detail import DetailView
# from urllib import request
# from videoClub.movie.models import Category, Movie
# from .models import Category, Movie
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .queries.movie_query import MovieQuery
from .models import Category, Movie
from .queries.pagination import Paginat
from .queries.path_request import PathRequest


# import pdb; pdb.set_trace()
# import pdb; pdb.set_trace()


def post_Home(request):
    # templates = 'home.html'
    #
    # if request.GET.get('movies'):
    #     movies = MovieQuery.filterMovies(request.GET.get('movies'))
    # elif request.GET.get('sort'):
    #     movies = MovieQuery.sortMovie(request.GET.get('sort'))
    # else:
    #     movies = MovieQuery.sortMovie(request.GET.get('/', ''))
    #
    # if movies:
    #     categories = Category.object.all()
    #     return render(request, templates, {'movies': movies, 'categories': categories})
    # else:
    #     templates = 'error_404.html'
    #     return render(request, templates)

    params = {'search': request.GET.get('search'), 'sort': request.GET.get('sort'), }
    # path = re.sub(r'page=\d+', '', params_as_string)
    movies_list = MovieQuery.filterRequest(params)
    categories = Category.object.all()

    if movies_list:
        movies = Paginat.getPaginator(movies_list, request.GET.get('page', ' '))
        path = PathRequest.getQueryWithout(request.GET.urlencode())
        return render(request, 'home.html', {'movies': movies, 'categories': categories, 'path': path})
    else:
        return render(request, 'request_not_found.html')


def detail_movies(request, pk):
    # movie = get_object_or_404(Movie, pk=pk)
    # return render(request, 'movie.html', {'movie': movie}x`x)
    params = {'pk': pk}
    movie = MovieQuery.filterRequest(params)

    if movie:
        return render(request, 'movie.html', {'movie': movie})
    else:
        return render(request, 'request_not_found.html')
    #
    # # return render(request, 'movie.html', {'movie': movie})


def detail_category(request, slug):
    # category = Category.object.get(slug=slug)
    #
    # if Movie.object.filter(category=category).exists():
    #     movies = Movie.object.filter(category=category).order_by("-created_date")
    # else:
    #     movies = None

    # return render(request, 'error_404.html')
    # if Category.object.filter(slug=slug).exists():
    params = {'slug': slug, 'search': request.GET.get('search'), 'sort': request.GET.get('sort'),
              'page': request.GET.get("page", ' '), }
    movies_list = MovieQuery.filterRequest(params)

    if movies_list:
        path = PathRequest.getQueryWithout(request.GET.urlencode())
        movies = Paginat.getPaginator(movies_list, request.GET.get('page', ' '))
        return render(request, "categories_detail.html", {'movies': movies, 'slug': slug, 'path': path})
    else:
        return render(request, 'request_not_found.html')


def random_movie(request):
    movie = Movie.object.order_by("?").first()
    path = "/movies/" + str(movie.pk) + "/"
    # return render(request, "movie.html", {'movie': movie})
    # pk = str(movie.pk) + '/'
    # response = redirect('/movie/' + pk, {'movie': movie})
    # return response
    return redirect(path)


def error_404(request):
    return render(request, '404.html')

# class HomeMoviesView(TemplateView):  # why ListView?
#     template_name = 'home.html'
#
#     def get_context_data(self, *args, **kwargs):
#         # pdb.set_trace()
#         context = super(HomeMoviesView, self).get_context_data(**kwargs)
#         context["movies"] = MovieQuery.result(self.request.GET.get('movies', ''))
#         context["categories"] = Category.object.all()
#
#         return context
# movies = Movie.object.all()
# categories = Category.object.all()
# def get(self, request):
#     manager = request.GET.get('manager', None)
#     if manager:
#         profiles_set = EmployeeProfile.objects.filter(manager=manager)
#     else:
#         profiles_set = EmployeeProfile.objects.all()
#         context = {
#             'profiles_set': profiles_set,
#             'title': 'Employee Profiles'
#         }


# class CategoryDetailView(DetailView):
#     model = Category
#     template_name = "category_detail.html"
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["categories"] = self.model.object.all()
#         # pdb.set_trace()
#         context["category"] = self.get_object()
#
#         return context


# class MovieView(DetailView):
#     model = Movie
#     template_name = "movie.html"
#
#     def get_context_data(self, *args, **kwargs):
#         # pdb.set_trace()
#         context = super().get_context_data(**kwargs)
#         context["movie"] = self.get_object()
#
#         return context
