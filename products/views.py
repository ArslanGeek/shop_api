from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category, Review
from .serializers import ProductSerializer, CategorySerializer, ReviewSerializer

@api_view(['GET'])
def product_list_api_view(request):
    product_list = Product.objects.all()
    data = ProductSerializer(instance=product_list, many=True).data
    return Response(data=data)

@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        product_detail = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Product not found'})
    data = ProductSerializer(instance=product_detail, many=False).data
    return Response(data=data)


@api_view(['GET'])
def category_list_api_view(request):
    category_list = Category.objects.all()
    data = CategorySerializer(instance=category_list, many=True).data
    return Response(data=data)

@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        category_detail = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Category not found'})
    data = CategorySerializer(instance=category_detail, many=False).data
    return Response(data=data)

@api_view(['GET'])
def review_list_api_view(request):
    review_list = Review.objects.all()
    data = ReviewSerializer(instance=review_list, many=True).data
    return Response(data=data)

@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review_detail = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Review not found'})
    data = ReviewSerializer(instance=review_detail, many=False).data
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
