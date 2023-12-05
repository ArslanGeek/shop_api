from django.contrib import admin
from .models import Product, Category, Review, Tag

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Tag)