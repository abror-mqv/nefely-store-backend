from rest_framework import serializers
from .models import Cpu

class CpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cpu
        fields = ("__all__")