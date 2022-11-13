from django.db import models

class Cpu(models.Model):
    name = models.CharField(verbose_name="Процессор", max_length=63)
    def __str__(self):
        return self.name