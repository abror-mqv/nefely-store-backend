from rest_framework import serializers
from .models import Cpu, Product

class CpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cpu
        fields = ("__all__")

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("__all__")