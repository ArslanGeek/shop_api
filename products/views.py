from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category, Review
from .serializers import ProductSerializer, \
    CategorySerializer, \
    ReviewSerializer, \
    ProductReviewSerializer, \
    ProductValidateSerializer, \
    CategoryValidateSerializer, \
    ReviewValidateSerializer

@api_view(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        product_list = Product.objects.all()
        data = ProductSerializer(instance=product_list, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = ProductValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        category_id = request.data.get('category_id')
        # tags = request.data.get('tags')
        tags = serializer.validated_data.get('tags')

        product = Product.objects.create(
            title=title, description=description, price=price, category_id=category_id
        )
        product.tags.set(tags)
        product.save()
        return Response(data={'product_id': product.id},
                        status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    try:
        product_detail = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Product not found'})
    if request.method == 'GET':
        data = ProductSerializer(instance=product_detail, many=False).data
        return Response(data=data)
    if request.method == 'PUT':
        serializer = ProductValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product_detail.title = request.data.get('title')
        product_detail.description = request.data.get('description')
        product_detail.price = request.data.get('price')
        product_detail.category_id = request.data.get('category_id')
        product_detail.save()
        return Response(data={'product_id': product_detail.id},
                        status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        product_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def category_list_api_view(request):
    if request.method == 'GET':
        category_list = Category.objects.all()
        data = CategorySerializer(instance=category_list, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = CategoryValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        name = request.data.get('name')
        category = Category.objects.create(
            name=name
        )
        category.save()
        return Response(data={'category_id': category.id},
                        status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, id):
    try:
        category_detail = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Category not found'})
    if request.method == 'GET':
        data = CategorySerializer(instance=category_detail, many=False).data
        return Response(data=data)
    if request.method == 'PUT':
        serializer = CategoryValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category_detail.name = request.data.get('name')
        category_detail.save()
        return Response(data={'category_id': category_detail.id},
                        status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        category_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        review_list = Review.objects.all()
        data = ReviewSerializer(instance=review_list, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        text = request.data.get('text')
        product_id = request.data.get('product_id')
        stars = request.data.get('stars')
        review = Review.objects.create(
            text=text, product_id=product_id, stars=stars
        )
        review.save()
        return Response(data={'review_id', review.id},
                        status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review_detail = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Review not found'})
    if request.method == 'GET':
        data = ReviewSerializer(instance=review_detail, many=False).data
        return Response(data=data)
    if request.method == 'PUT':
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        review_detail.text = request.data.get('text')
        review_detail.product_id = request.data.get('product_id')
        review_detail.stars = request.data.get('stars')
        review_detail.save()
        return Response(data={'review_id', review_detail.id},
                        status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        review_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET'])
# def products_review_api_view(request):
#     products_review_list = Review.objects.all()
#     data = ReviewSerializer(instance=products_review_list, many=True).data
#     return Response(data=data)


@api_view(['GET'])
def product_review_list_api_view(request):
    queryset = Product.objects.all()
    data = ProductReviewSerializer(queryset, many=True).data
    return Response(data=data)


# @api_view(['GET'])
# def products_api_view(request):
#     dict_ = {
#         'text': 'Weclome to the SHOP',
#         'integer': 1000,
#         'bool': True,
#         'list': [1, 2, 3],
#         'dict': {'key', 'value'}
#     }
#     return Response(data=dict_)
