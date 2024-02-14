from django.shortcuts import render

# Create your views here.
# smart_library/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Book, Rating
from .serializers import BookSerializer, RatingSerializer
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework import status

class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        search_term = request.query_params.get('search', '')
        sort_by = request.query_params.get('sort', '')

        queryset = Book.objects.filter(
            Q(title__icontains=search_term) | Q(author__icontains=search_term)
        )


        if sort_by == 'popularity':
            queryset = queryset.order_by('-popularity')
        elif sort_by == 'rating':
            queryset = queryset.order_by('-rating')
        else:
            # Default sorting if no sort parameter is provided
            queryset = queryset.order_by('title')

        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

class RatingCreateAPIView(APIView):
    def post(self, request):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookRatingAPIView(APIView):
    def get(self, request, book_id, user_id):
        try:
            rating = Rating.objects.get(book_id=book_id, user=user_id)
            serializer = RatingSerializer(rating)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Rating.DoesNotExist:
            return Response({"message": "Rating not found for the specified book and user"}, status=status.HTTP_404_NOT_FOUND)
