from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, ProductPaginationViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'product-pagination', ProductPaginationViewSet, basename='product-pagination')

urlpatterns = [
    path('api/', include(router.urls)),
]
