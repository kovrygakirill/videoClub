from django.conf.urls import url
# from videoClub.movie.views import CategoryListView --- WRONG
from .views import CategoryListView

urlpatterns = [
    url(r'^$', CategoryListView.as_view())
]