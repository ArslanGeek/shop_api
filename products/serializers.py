from rest_framework import serializers
from .models import Category, Product, Review, Tag
from rest_framework.exceptions import ValidationError


class TagValidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name")


class ProductSerializer(serializers.ModelSerializer):
    tags = TagValidateSerializer(many=True)
    class Meta:
        model = Product
        fields = ("id", "title", "description", "price", "category", "tags")

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

class ProductValidateSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(max_length=100)
    # description = serializers.CharField(required=False)
    # price = serializers.IntegerField(min_value=1)
    category_id = serializers.IntegerField(min_value=1)
    tags = serializers.ListField(child=serializers.IntegerField(), required=False)

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'category_id', 'tags')

    def validate_tags(self, value: list):
        for tag_id in value:
            try:
                Tag.objects.get(id=tag_id)
            except Tag.DoesNotExist:
                raise serializers.ValidationError(f'Тег с id {tag_id} не найден!')
        return value

    # def validate_tags(self, value: list):
    #     for tag_id in value:
    #         try:
    #             Tag.objects.get(id=tag_id)
    #         except Tag.DoesNotExist:
    #             raise serializers.ValidationError(f'Tag with id {tag_id} does not exists')
    #     return value

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category does not exists')
        return category_id

class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    product_id = serializers.IntegerField(min_value=1)
    stars = serializers.IntegerField(min_value=1, max_value=5)

    def validate_product_id(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError('Product does not exists')
        return product_id










