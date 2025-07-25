# Generated by Django 5.2.4 on 2025-07-18 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='no_in_stock',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='reviews',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
