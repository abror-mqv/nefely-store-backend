from django.shortcuts import render
from rest_framework import generics
from .models import Cpu, Product
from .serializers import CpuSerializer, ProductSerializer
# Create your views here.

class CpuApiView(generics.ListAPIView):
    queryset = Cpu.objects.all()
    serializer_class = CpuSerializer

class ProductsApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
