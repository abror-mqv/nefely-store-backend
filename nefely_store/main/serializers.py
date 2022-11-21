from rest_framework import serializers
from rest_framework.views import APIView
from .models import Product, Compilation
from rest_framework.response import Response

class ProductSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Product
        fields = ("__all__")

class CompilationSerializer(serializers.ModelSerializer):
    publications = ProductSerializer(read_only = True, many = True)
    class Meta:
        model = Compilation
        fields = ("__all__")  
        
class CategSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compilation
        fields = ()


