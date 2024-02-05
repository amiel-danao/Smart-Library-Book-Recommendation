from django.shortcuts import render

# Create your views here.
# smart_library/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        title = request.query_params.get('title', '')
        author = request.query_params.get('author', '')

        queryset = Book.objects.filter(title__icontains=title, author__icontains=author)
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)
