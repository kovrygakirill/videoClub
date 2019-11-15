from django.conf.urls import url
# from videoClub.movie.views import CategoryListView --- WRONG
from .views import post_Home, detail_movies, detail_category, error_404

handler404 = error_404

urlpatterns = [
    # url(r'^$', HomeMoviesView.as_view(), name="base_view"),
    # url(r'^category/(?P<slug>[-\w]+)/$', CategoryDetailView.as_view(), name="category-detail"),
    # url(r'^movies/(?P<pk>[0-9]+)/$', MovieView.as_view(), name="movie_view"),
    url(r'^$', post_Home, name="post_Home"),
    url(r'^category/(?P<slug>[-\w]+)/$', detail_category, name="detail_category"),
    url(r'^movies/(?P<pk>[0-9]+)/$', detail_movies, name="detail_movies"),
]
