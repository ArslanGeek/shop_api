# Generated by Django 4.2.7 on 2023-11-24 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_count_review_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.PositiveIntegerField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], null=True),
        ),
    ]
