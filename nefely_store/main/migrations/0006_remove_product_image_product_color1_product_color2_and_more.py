# Generated by Django 4.1.3 on 2022-11-14 11:46

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='color1',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None),
        ),
        migrations.AddField(
            model_name='product',
            name='color2',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None),
        ),
        migrations.AddField(
            model_name='product',
            name='color3',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None),
        ),
        migrations.AddField(
            model_name='product',
            name='color4',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None),
        ),
        migrations.AddField(
            model_name='product',
            name='color5',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None),
        ),
        migrations.AddField(
            model_name='product',
            name='color_name1',
            field=models.CharField(default=None, max_length=31, verbose_name='Наименование цвета 1'),
        ),
        migrations.AddField(
            model_name='product',
            name='color_name2',
            field=models.CharField(default=None, max_length=31, verbose_name='Наименование цвета 2'),
        ),
        migrations.AddField(
            model_name='product',
            name='color_name3',
            field=models.CharField(default=None, max_length=31, verbose_name='Наименование цвета 3'),
        ),
        migrations.AddField(
            model_name='product',
            name='color_name4',
            field=models.CharField(default=None, max_length=31, verbose_name='Наименование цвета 4'),
        ),
        migrations.AddField(
            model_name='product',
            name='color_name5',
            field=models.CharField(default=None, max_length=31, verbose_name='Наименование цвета 5'),
        ),
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(default=None, upload_to='', verbose_name='Изображение 1'),
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(default=None, upload_to='', verbose_name='Изображение 2'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(default=None, upload_to='', verbose_name='Изображение 3'),
        ),
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(default=None, upload_to='', verbose_name='Изображение 4'),
        ),
        migrations.AddField(
            model_name='product',
            name='image5',
            field=models.ImageField(default=None, upload_to='', verbose_name='Изображение 5'),
        ),
    ]