from django.contrib import admin
from .models import Cpu, Manufacter, Compilation, Product

admin.site.register([Cpu, Manufacter, Compilation, Product])

