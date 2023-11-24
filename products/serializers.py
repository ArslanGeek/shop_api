from rest_framework import serializers
from .models import Category, Product, Review




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id title price reviews'.split()

class CategorySerializer(serializers.ModelSerializer):
    product_type = ProductSerializer(many=True, read_only=True)
    product_count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = 'name product_count product_type'.split()

    def get_product_count(self, obj):
        return obj.product_type.count()





class ReviewSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ('product_name', 'text', 'stars')

    def get_product_name(self, obj):
        return obj.product.title

class ProductReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    def get_average_rating(self, obj):
        total_stars = sum(review.stars for review in obj.reviews.all())
        num_reviews = obj.reviews.count()
        if num_reviews > 0:
            return total_stars / num_reviews
        else:
            return 0.0

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'category', 'reviews', 'average_rating')






