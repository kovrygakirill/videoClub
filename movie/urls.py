from django.conf.urls import url
# from videoClub.movie.views import CategoryListView --- WRONG
from .views import post_Home, detail_movies, detail_category, error_404, random_movie
from .views import addLike,addDislike
from django.views.decorators.csrf import csrf_exempt
# handler404 = error_404

urlpatterns = [
    # url(r'^$', HomeMoviesView.as_view(), name="base_view"),
    # url(r'^category/(?P<slug>[-\w]+)/$', CategoryDetailView.as_view(), name="category-detail"),
    # url(r'^movies/(?P<pk>[0-9]+)/$', MovieView.as_view(), name="movie_view"),
    url(r'^$', post_Home, name="post_Home"),
    url(r'^add_like/$', csrf_exempt(addLike), name="add_like"),
    url(r'^add_dislike/$', csrf_exempt(addDislike), name="add_dislike"),
    url(r'^category/(?P<slug>[\w]+)/$', detail_category, name="detail_category"),
    url(r'^movies/(?P<pk>\d+)/$', detail_movies, name="detail_movies"),
    url(r'^random_movie/$', random_movie, name="random_movie"),
    # url(r'^sort/$', detail_movies, name="detail_movies"),
    url(r'^(?!media).*$', error_404, name="404")
]
