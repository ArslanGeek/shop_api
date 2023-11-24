from django.db import models


# Create your models here.
# class Count(models.Model):
#     count = (
#         ('1', 1),
#         ('2', 2),
#         ('3', 3),
#         ('4', 4),
#         ('5', 5),
#     )



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='product_type')
    created = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f'{self.title} {self.price}$'

class Review(models.Model):

    text = models.TextField(null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='reviews')
    stars = models.PositiveIntegerField(null=True, verbose_name="Rating (1 - 5)", default=1, choices=[(i, i * '*') for i in range(1, 6)])
    # stars = models.PositiveIntegerField(null=True, choices=Count.count)






    def __str__(self):
        return f'{self.product}'




