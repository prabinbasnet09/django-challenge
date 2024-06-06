from rest_framework.generics import ListCreateAPIView

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieListView(ListCreateAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        runtime = self.request.query_params.get("runtime")
        runtime_lt = self.request.query_params.get("runtime_lt")
        runtime_gt = self.request.query_params.get("runtime_gt")

        if runtime:
            return Movie.objects.filter(runtime=runtime).order_by("id")
        if runtime_lt:
            return Movie.objects.filter(runtime__lt=runtime_lt).order_by("id")
        if runtime_gt:
            return Movie.objects.filter(runtime__gt=runtime_gt).order_by("id")
