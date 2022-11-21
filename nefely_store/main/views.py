#ГЛЕНТ ЧОРТ
#ТИЛЯ ЧОРТ

from rest_framework import generics, viewsets
from rest_framework.response import Response
from .models import Product, Compilation
from .serializers import ProductSerializer, CompilationSerializer
from rest_framework.views import APIView
from django.forms import model_to_dict
import json
# Create your views here.

class ProductsApiView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CompilationsApiView(viewsets.ModelViewSet):
    queryset = Compilation.objects.all()
    serializer_class = CompilationSerializer

class GetProductsApiView(APIView):
    def get(request, self, *args, **kwargs): 
        pl = Product.objects.all().values()
        return Response({"compilations": list(pl)})       