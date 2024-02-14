# smart_library/models.py
from django.db import models

class Book(models.Model):
    author = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255, null=True)
    year = models.PositiveIntegerField(default=0, null=True)
    popularity = models.PositiveIntegerField(default=0, null=True)
    rating = models.FloatField(default=0, null=True)  # Add default value for rating
    course = models.CharField(max_length=100, null=True)
    total_rating = models.FloatField(default=0, null=True)  # New field for total rating
    rating_count = models.PositiveIntegerField(default=0, null=True)  # New field for rating count
    # image = models.ImageField(upload_to='book_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

    def save(self, *args, **kwargs):
        # Update rating based on total_rating and rating_count
        if self.rating_count > 0:
            self.rating = self.total_rating / self.rating_count
        else:
            self.rating = 0
        super().save(*args, **kwargs)


class Rating(models.Model):
    user = models.CharField(default="", max_length=300, null=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveIntegerField(default=0, null=True)

    class Meta:
        unique_together = ('user', 'book')