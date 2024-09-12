# from django.shortcuts import render, get_object_or_404
# from .models import Product, Category
#
#
# def product_list(request):
#     products = Product.objects.filter(available=True)
#     categories = Category.objects.all()
#     return render(request, 'product_list.html', {'products': products, 'categories': categories})
#
#
# def product_detail(request, id):
#     product = get_object_or_404(Product, id=id)
#     return render(request, 'product_detail.html', {'product': product})
#
#
# def product_search(request):
#     query = request.GET.get('q')
#     products = Product.objects.filter(name__icontains=query) | Product.objects.filter(description__icontains=query)
#     return render(request, 'product_search.html', {'products': products, 'query': query})
#
#
# def category_products(request, category_id):
#     category = get_object_or_404(Category, id=category_id)
#     products = Product.objects.filter(category=category, available=True)
#     return render(request, 'category_products.html', {'category': category, 'products': products})


# from rest_framework import viewsets
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
#
# from .Pagination import CustomPagination
# from .models import Product, Category
# from .serializers import ProductSerializer, CategorySerializer
# from rest_framework.decorators import action
#
#
# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.filter(available=True)
#     serializer_class = ProductSerializer
#     pagination_class = CustomPagination
#
#     @action(detail=False, methods=['get'])
#     def search(self, request):
#         query = request.query_params.get('q', None)
#         if query:
#             products = Product.objects.filter(name__icontains=query) | Product.objects.filter(
#                 description__icontains=query)
#             page = self.paginate_queryset(products)
#             if page is not None:
#                 serializer = self.get_serializer(page, many=True)
#                 return self.get_paginated_response(serializer.data)
#             serializer = self.get_serializer(products, many=True)
#             return Response(serializer.data)
#         return Response({"message": "No query provided"}, status=400)
#
#     @action(detail=False, methods=['get'], url_path='category/<int:category_id>')
#     def category_products(self, request, category_id=None):
#         category = get_object_or_404(Category, id=category_id)
#         products = Product.objects.filter(category=category, available=True)
#         page = self.paginate_queryset(products)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#         serializer = self.get_serializer(products, many=True)
#         return Response(serializer.data)
#
#
# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .Pagination import CustomPagination
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.decorators import action


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', None)
        if query:
            products = Product.objects.filter(name__icontains=query) | Product.objects.filter(
                description__icontains=query)
            page = self.paginate_queryset(products)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(products, many=True)
            return Response(serializer.data)
        return Response({"message": "No query provided"}, status=400)

    @action(detail=False, methods=['get'], url_path='category/<int:category_id>')
    def category_products(self, request, category_id=None):
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category, available=True)
        page = self.paginate_queryset(products)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
