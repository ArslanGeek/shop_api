# Generated by Django 4.2.7 on 2023-11-23 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_review_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='title',
        ),
    ]
