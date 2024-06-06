from rest_framework import serializers

from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    runtime_formatted = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "runtime",
            "release_date",
            "runtime_formatted"
        )
    
    def get_runtime_formatted(self, obj):
        hours, minutes = divmod(obj.runtime, 60)
        return f"{hours}:{minutes:02d}"