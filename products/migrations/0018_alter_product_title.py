# Generated by Django 4.2.7 on 2023-12-05 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_alter_product_options_alter_product_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]