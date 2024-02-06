# smart_library/models.py
from django.db import models

class Book(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    popularity = models.PositiveIntegerField()
    rating = models.FloatField(default=0)  # Add default value for rating
    course = models.CharField(max_length=100)
    total_rating = models.FloatField(default=0)  # New field for total rating
    rating_count = models.PositiveIntegerField(default=0)  # New field for rating count

    def __str__(self):
        return f"{self.title} by {self.author}"

    def save(self, *args, **kwargs):
        # Update rating based on total_rating and rating_count
        if self.rating_count > 0:
            self.rating = self.total_rating / self.rating_count
        else:
            self.rating = 0
        super().save(*args, **kwargs)