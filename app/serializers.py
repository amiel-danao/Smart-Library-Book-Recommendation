# smart_library/serializers.py
from rest_framework import serializers
from .models import Book
from .models import Rating

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'author', 'title', 'year', 'popularity', 'rating', 'course']




class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['user', 'book', 'rating']
    
    def validate(self, data):
        # Ensure user and book are provided
        if 'user' not in data:
            raise serializers.ValidationError("User is required.")
        if 'book' not in data:
            raise serializers.ValidationError("Book is required.")
        return data