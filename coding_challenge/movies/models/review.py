from django.db import models
from django.core.exceptions import ValidationError

def validate_rating(value):
    if value < 1 or value > 5:
        raise ValidationError("Rating must be between 1 and 5")

class Review(models.Model):
    movie = models.ForeignKey("Movie", on_delete = models.CASCADE, related_name="reviewers")
    name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(validators=[validate_rating])