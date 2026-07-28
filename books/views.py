from django.shortcuts import render

# Create your views here.

from rest_framework import filters, viewsets

from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        'title',
        'author',
        'isbn',
    ]

    ordering_fields = [
        'title',
        'price',
        'stock',
        'created_at'
    ]

    ordering = ('-created_at',)