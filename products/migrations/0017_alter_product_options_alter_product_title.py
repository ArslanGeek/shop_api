# Generated by Django 4.2.7 on 2023-12-05 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_product_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created',), 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
