from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Product, Category


class ProductTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Category 1")
        self.product = Product.objects.create(
            name="Product 1",
            description="Description of Product 1",
            price=100.00,
            category=self.category
        )

    def test_get_product_list(self):
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)

    # def test_get_product_detail(self):
    #     print(f"Product ID: {self.product.id}")
    #     url = reverse('product-detail', args=[self.product.id])
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, self.product.name)

    def test_product_search(self):
        url = reverse('product-search')
        response = self.client.get(url, {'q': 'Product 1'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Product 1')

    def test_category_products(self):
        url = reverse('category-list')  # Ensure this matches the registered URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Category 1')
