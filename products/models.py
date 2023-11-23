from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} {self.price}$'

class Review(models.Model):
    text = models.TextField(null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.product}'

