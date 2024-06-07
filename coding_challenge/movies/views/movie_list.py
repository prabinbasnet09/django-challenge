from rest_framework.generics import ListCreateAPIView

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieListView(ListCreateAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.all()
        runtime = self.request.query_params.get("runtime")
        runtime_lt = self.request.query_params.get("runtime_lt")
        runtime_gt = self.request.query_params.get("runtime_gt")

        if runtime:
            queryset = Movie.objects.filter(runtime=runtime)
        if runtime_lt:
            queryset = Movie.objects.filter(runtime__lt=runtime_lt)
        if runtime_gt:
            queryset = Movie.objects.filter(runtime__gt=runtime_gt)

        return queryset.order_by("id")