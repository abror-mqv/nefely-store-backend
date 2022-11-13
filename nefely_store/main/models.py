from django.db import models

class Cpu(models.Model):
    name = models.CharField(verbose_name="Процессор", max_length=63)
    def __str__(self):
        return self.name

class Rom(models.Model):
    name = models.CharField(verbose_name="Память", max_length=31)
    def __str__(self):
        return self.name

class Manufacter(models.Model):
    name =  models.CharField(verbose_name="Производитель", max_length=31)
    def __str__(self):
        return self.name

class Compilation(models.Model):
    name = models.CharField(verbose_name="Подборка", max_length=127)
    def __str__(self):
        return self.name



class Product(models.Model):
    char_name = models.CharField(verbose_name="Название телефона", max_length=127)
    compilations = models.ManyToManyField(Compilation, verbose_name="Участие в подборках")
    price = models.CharField(verbose_name="Цена", max_length=127)


    def __str__(self):
        return self.char_name
    
    