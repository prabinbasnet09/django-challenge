from django.contrib import admin

from movies.models import Movie 
from movies.models import Review

@admin.register(Movie)
class MovieAdminConsole(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "runtime",
        "release_date",
    )

@admin.register(Review)
class ReviewAdminConsole(admin.ModelAdmin):
    list_display = (
        "id",
        "movie",
        "name",
        "rating",
    )

