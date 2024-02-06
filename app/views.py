from django.shortcuts import render

# Create your views here.
# smart_library/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from django.db.models import Q

class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        search_term = request.query_params.get('search', '')
        sort_by = request.query_params.get('sort', '')

        queryset = Book.objects.filter(Q(title__icontains=search_term) | Q(author__icontains=search_term))

        if sort_by == 'popularity':
            queryset = queryset.order_by('-popularity')
        elif sort_by == 'rating':
            queryset = queryset.order_by('-rating')

        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)
