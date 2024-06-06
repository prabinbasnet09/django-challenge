from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100, unique=True)
    runtime = models.PositiveIntegerField()
    release_date = models.DateField()

    def get_avg_rating(self):
        reviewers = self.reviewers.all()
        if not reviewers:
            return None
        return round(reviewers.aggregate(models.Avg("rating"))["rating__avg"], 2)
        
