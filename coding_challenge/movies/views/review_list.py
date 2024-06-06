from rest_framework.generics import ListCreateAPIView, ValidationError

from movies.models import Review
from movies.serializers import ReviewSerializer

from movies.models import Movie

class ReviewListView(ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        movie_id = self.kwargs.get("movie_id")
        return Review.objects.filter(movie_id=movie_id)
    
    def perform_create(self, serializer):
        movie_id = self.kwargs.get("movie_id")
        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValidationError({"movie_id": "Movie with the give id does not exist."})
        serializer.save(movie=movie)