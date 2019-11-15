from django.shortcuts import render

# from django.views.generic import TemplateView
# from django.views.generic.list import ListView
# from .models import Category, Movie
# from django.views.generic.detail import DetailView
# from urllib import request
from .models import Category, Movie
from .queries.movie_query import MovieQuery


# import pdb; pdb.set_trace()


def post_Home(request):
    movies = MovieQuery.result(request.GET.get('movies', ''))
    categories = Category.object.all()

    return render(request, 'home.html', {'movies': movies, 'categories': categories})


def detail_movies(request, pk):
    if Movie.object.filter(pk=pk).exists():
        movie = Movie.object.get(pk=pk)
        return render(request, 'movie.html', {'movie': movie})
    else:
        return render(request, 'error_404.html')


def detail_category(request, slug):
    category = Category.object.get(slug=slug)

    if Movie.object.filter(category=category).exists():
        movies = Movie.object.filter(category=category).order_by("-created_date")
    else:
        movies = None

    return render(request, "categories_detail.html", {'movies': movies})


def error_404(request, exception):
    return render(request, 'error_404.html')

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
