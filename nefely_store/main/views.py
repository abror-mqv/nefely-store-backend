from django.shortcuts import render
from rest_framework import generics
from .models import Cpu
from .serializers import CpuSerializer
# Create your views here.

class CpuApiView(generics.ListAPIView):
    queryset = Cpu.objects.all()
    serializer_class = CpuSerializer
