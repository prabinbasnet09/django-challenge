from rest_framework import serializers

from movies.models import Movie
from movies.serializers.review_serializer import ReviewSerializer


class MovieSerializer(serializers.ModelSerializer):
    runtime_formatted = serializers.SerializerMethodField()
    reviewers = ReviewSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "runtime",
            "release_date",
            "runtime_formatted",
            "reviewers",
            "avg_rating",
        )
    
    def get_runtime_formatted(self, obj):
        hours, minutes = divmod(obj.runtime, 60)
        return f"{hours}:{minutes:02d}"
    
    def get_avg_rating(self, obj):
        return obj.get_avg_rating()