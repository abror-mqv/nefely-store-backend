# Generated by Django 4.1.3 on 2022-11-14 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_book_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='book',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='mem1',
            field=models.CharField(default=0, max_length=31, verbose_name='Объем памяти 1'),
        ),
        migrations.AddField(
            model_name='product',
            name='mem2',
            field=models.CharField(default=0, max_length=31, verbose_name='Объем памяти 2'),
        ),
        migrations.AddField(
            model_name='product',
            name='mem3',
            field=models.CharField(default=0, max_length=31, verbose_name='Объем памяти 3'),
        ),
        migrations.AddField(
            model_name='product',
            name='mem4',
            field=models.CharField(default=0, max_length=31, verbose_name='Объем памяти 5'),
        ),
        migrations.AddField(
            model_name='product',
            name='mem5',
            field=models.CharField(default=0, max_length=31, verbose_name='Объем памяти 4'),
        ),
        migrations.AddField(
            model_name='product',
            name='price_1',
            field=models.CharField(default=0, max_length=127, verbose_name='Цена 1'),
        ),
        migrations.AddField(
            model_name='product',
            name='price_2',
            field=models.CharField(default=0, max_length=127, verbose_name='Цена 2'),
        ),
        migrations.AddField(
            model_name='product',
            name='price_3',
            field=models.CharField(default=0, max_length=127, verbose_name='Цена 3'),
        ),
        migrations.AddField(
            model_name='product',
            name='price_4',
            field=models.CharField(default=0, max_length=127, verbose_name='Цена 4'),
        ),
        migrations.AddField(
            model_name='product',
            name='price_5',
            field=models.CharField(default=0, max_length=127, verbose_name='Цена 5'),
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]