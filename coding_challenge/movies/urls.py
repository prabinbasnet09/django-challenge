from django.urls import path

from movies.views import MovieListView
from movies.views import MovieDetailView
from movies.views import ReviewListView

urlpatterns = [
    path("", MovieListView.as_view(), name="MovieListView"),
    path("<int:pk>/",MovieDetailView.as_view(), name="MovieDetailView"),
    path("<int:movie_id>/reviews/", ReviewListView.as_view(), name="ReviewListView"),
]
