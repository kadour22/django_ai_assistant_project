from rest_framework import generics
from .models import products
from .serializers import ProductSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = products.objects.all()
    serializer_class = ProductSerializer