# Generated by Django 4.2.7 on 2023-11-23 13:35

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.TextField(null=True, verbose_name=products.models.Product),
        ),
    ]
