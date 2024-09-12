# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.product_list, name='product_list'),
#     path('product/<int:id>/', views.product_detail, name='product_detail'),
#     path('search/', views.product_search, name='product_search'),
#     path('category/<int:category_id>/', views.category_products, name='category_products'),
# ]

# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('api/', include(router.urls)),
]
