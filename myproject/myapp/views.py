from django.shortcuts import render
from rest_framework import generics

from myapp.models import Category, Product
from myapp.serializers import CategorySerializer, ProductSerializer

# Create your views here.

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class= CategorySerializer
    
class CategoryDetail(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

def index(request):
    return render(request , 'index.html')

# booking/views.py
from django.shortcuts import render

from .models import Booking, Movie


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movie_detail.html', {'movie': movie})

def book_ticket(request, movie_id):
    if request.method == 'POST':
        # Handle form submission to book ticket
        # Update seat availability, create booking entry, etc.
        # Redirect to confirmation page
        pass
    else:
        movie = Movie.objects.get(id=movie_id)
        return render(request, 'book_ticket.html', {'movie': movie})
