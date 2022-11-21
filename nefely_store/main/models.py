from django.db import models
from colorfield.fields import ColorField
from mptt.models import MPTTModel, TreeForeignKey


class Cpu(models.Model):
    name = models.CharField(verbose_name="Процессор", max_length=63)

    def __str__(self):
        return self.name


class Manufacter(models.Model):
    name = models.CharField(verbose_name="Производитель", max_length=31)

    def __str__(self):
        return self.name


class Product(models.Model):
    char_name = models.CharField(
        verbose_name="Название телефона", max_length=127)
    # cpu = models.TreeForeignKey(Cpu, on_delete=models.PROTECT, default=None)

    roarCam = models.CharField(
        verbose_name="Задняя камера", max_length=31, default=None)
    frontCam = models.CharField(
        verbose_name="Фронтальная камера", max_length=31, default=None)

    mem1 = models.CharField(
        verbose_name="Объем памяти 1", max_length=31, default=0)
    price_1 = models.CharField(
        verbose_name="Цена 1", max_length=127, default=0
    )
    mem2 = models.CharField(
        verbose_name="Объем памяти 2", max_length=31, default=0, null=True, blank=True)
    price_2 = models.CharField(
        verbose_name="Цена 2", max_length=127, default=0, null=True, blank=True)
    mem3 = models.CharField(
        verbose_name="Объем памяти 3", max_length=31, default=0, null=True, blank=True)
    price_3 = models.CharField(
        verbose_name="Цена 3", max_length=127, default=0, null=True, blank=True)
    mem5 = models.CharField(
        verbose_name="Объем памяти 4", max_length=31, default=0, null=True, blank=True)
    price_4 = models.CharField(
        verbose_name="Цена 4", max_length=127, default=0, null=True, blank=True)
    mem4 = models.CharField(
        verbose_name="Объем памяти 5", max_length=31, default=0, null=True, blank=True)
    price_5 = models.CharField(
        verbose_name="Цена 5", max_length=127, default=0, null=True, blank=True)

    color_name1 = models.CharField(
        verbose_name="Наименование цвета 1", max_length=31, default=None)
    image1 = models.ImageField(verbose_name="Изображение 1", default=None)
    color1 = ColorField(default='#FFFFFF')

    color_name2 = models.CharField(
        verbose_name="Наименование цвета 2", max_length=31, default=None, null=True, blank=True)
    image2 = models.ImageField(
        verbose_name="Изображение 2", default=None, null=True, blank=True)
    color2 = ColorField(default='#FFFFFF', null=True, blank=True)

    color_name3 = models.CharField(
        verbose_name="Наименование цвета 3", max_length=31, default=None, null=True, blank=True)
    image3 = models.ImageField(
        verbose_name="Изображение 3", default=None, null=True, blank=True)
    color3 = ColorField(default='#FFFFFF', null=True, blank=True)

    color_name4 = models.CharField(
        verbose_name="Наименование цвета 4", max_length=31, default=None, null=True, blank=True)
    image4 = models.ImageField(
        verbose_name="Изображение 4", default=None, null=True, blank=True)
    color4 = ColorField(default='#FFFFFF', null=True, blank=True)

    color_name5 = models.CharField(
        verbose_name="Наименование цвета 5", max_length=31, default=None, null=True, blank=True)
    image5 = models.ImageField(
        verbose_name="Изображение 5", default=None, null=True, blank=True)
    color5 = ColorField(default='#FFFFFF', null=True, blank=True)

    description = models.TextField(
        verbose_name="Описание", max_length=255, default=None)

    def __str__(self):
        return self.char_name
  

class Compilation(models.Model):    
    name = models.CharField(verbose_name="Подборка", max_length=127, default=None)   
    color = ColorField(default='#FF0000')
    publications = models.ManyToManyField(Product, related_name="PUBLICATIONS", verbose_name="dadew")
    hookid = models.CharField(
        verbose_name="Якорь", max_length=31, default=None, null=True, blank=True)    
    def __str__(self):
        return self.name
