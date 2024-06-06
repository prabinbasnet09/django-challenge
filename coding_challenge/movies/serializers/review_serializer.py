from rest_framework import serializers

from movies.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            "name",
            "rating"
        )