from rest_framework import serializers
from .models import Product, ProductImage, Category


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class ProductSerializer(serializers.ModelSerializer):
    formatted_price = serializers.SerializerMethodField()
    images = ProductImageSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'category', 'available', 'formatted_price', 'images']

    def get_formatted_price(self, obj):
        return obj.formatted_price()
