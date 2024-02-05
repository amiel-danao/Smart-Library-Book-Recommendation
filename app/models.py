# smart_library/models.py
from django.db import models

class Book(models.Model):
    author = models.CharField(max_length=255, default='', null=True, blank=True)
    title = models.CharField(max_length=255, default='', null=True, blank=True)
    year = models.PositiveIntegerField(default=0, blank=True)
    popularity = models.PositiveIntegerField(default=0, blank=True)
    rating = models.PositiveIntegerField(default=0, blank=True)
    course = models.CharField(max_length=100, default='', null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
