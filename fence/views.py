from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .Pagination import CustomPagination
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.decorators import action
from django.db.models import Q


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q')
        if not query:
            return Response({"message": "No query provided"}, status=400)

        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

        page = self.paginate_queryset(products)
        serializer = self.get_serializer(page, many=True) if page else self.get_serializer(products, many=True)
        return self.get_paginated_response(serializer.data) if page else Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='category/(?P<category_id>\d+)')
    def category_products(self, request, category_id=None):
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category, available=True)

        page = self.paginate_queryset(products)
        serializer = self.get_serializer(page, many=True) if page else self.get_serializer(products, many=True)
        return self.get_paginated_response(serializer.data) if page else Response(serializer.data)

    @action(detail=True, methods=['get'])
    def detail(self, request, pk=None):
        product = self.get_object()  # Retrieves the product based on `pk`
        serializer = self.get_serializer(product)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductPaginationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q')
        if not query:
            return Response({"message": "No query provided"}, status=400)

        products = Product.objects.filter(
            name__icontains=query
        ) | Product.objects.filter(
            description__icontains=query
        )

        page = self.paginate_queryset(products)
        serializer = self.get_serializer(page, many=True) if page else self.get_serializer(products, many=True)
        return self.get_paginated_response(serializer.data) if page else Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='category/(?P<category_id>\d+)')
    def category_products(self, request, category_id=None):
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category, available=True)

        page = self.paginate_queryset(products)
        serializer = self.get_serializer(page, many=True) if page else self.get_serializer(products, many=True)
        return self.get_paginated_response(serializer.data) if page else Response(serializer.data)

    @action(detail=True, methods=['get'])
    def detail(self, request, pk=None):
        product = self.get_object()
        serializer = self.get_serializer(product)
        return Response(serializer.data)
