from django.contrib import admin
from .models import Cpu, Rom, Manufacter, Compilation, Product, Book, Review

admin.site.register([Cpu, Rom, Manufacter, Compilation, Product, Book, Review])

class ReviewInline(admin.StackedInline):
    model = Review

class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]