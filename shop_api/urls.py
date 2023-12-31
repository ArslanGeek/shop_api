"""
URL configuration for shop_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from products import views
from users import views as users_views
from . import swagger

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/categories/', views.category_list_api_view),
    # path('api/v1/categories/<int:id>/', views.category_detail_api_view),
    path('api/v1/categories/', views.CategoryListCreateAPIView.as_view()),
    path('api/v1/categories/<int:id>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    # path('api/v1/products/', views.product_list_api_view),
    # path('api/v1/products/<int:id>/', views.product_detail_api_view),
    path('api/v1/products/', views.ProductListCreateAPIView.as_view()),
    path('api/v1/products/<int:id>/', views.ProductRetrieveUpdateDestroyAPIView.as_view()),
    # path('api/v1/reviews/', views.review_list_api_view),
    # path('api/v1/reviews/<int:id>/', views.review_detail_api_view),
    path('api/v1/reviews/', views.ReviewListCreateAPIView.as_view()),
    path('api/v1/reviews/<int:id>/', views.ReviewRetrieveUpdateDestroyAPIView.as_view()),
    # path('api/v1/products/review/', views.product_review_list_api_view),
    path('api/v1/products/review/', views.ProductReviewListCreateAPIView.as_view()),
    # path('api/v1/users/register/', users_views.register_api_view),
    path('api/v1/users/register/', users_views.UserRegisterAPIView.as_view()),
    # path('api/v1/users/login/', users_views.login_api_view),
    # path('api/v1/users/confirm/', users_views.confirm_user_api_view),
    path('api/v1/users/login/', users_views.UserLoginAPIView.as_view()),
    path('api/v1/users/confirm/', users_views.UserConfirmAPIView.as_view()),


]

urlpatterns += swagger.urlpatterns
