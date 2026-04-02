import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_back.settings')
django.setup()

from api.models import Category, Product

# Create categories
categories = [
    {'name': 'Electronics'},
    {'name': 'Clothing'},
    {'name': 'Books'},
    {'name': 'Home & Garden'},
]

for cat_data in categories:
    Category.objects.get_or_create(**cat_data)

# Get categories
electronics = Category.objects.get(name='Electronics')
clothing = Category.objects.get(name='Clothing')
books = Category.objects.get(name='Books')
home_garden = Category.objects.get(name='Home & Garden')

# Create products
products = [
    # Electronics
    {'name': 'Laptop', 'price': 999.99, 'description': 'High-performance laptop', 'count': 10, 'category': electronics},
    {'name': 'Smartphone', 'price': 699.99, 'description': 'Latest smartphone', 'count': 20, 'category': electronics},
    {'name': 'Headphones', 'price': 199.99, 'description': 'Wireless headphones', 'count': 15, 'category': electronics},
    {'name': 'Tablet', 'price': 399.99, 'description': '10-inch tablet', 'count': 12, 'category': electronics},
    {'name': 'Smart Watch', 'price': 299.99, 'description': 'Fitness smart watch', 'count': 8, 'category': electronics},

    # Clothing
    {'name': 'T-Shirt', 'price': 19.99, 'description': 'Cotton t-shirt', 'count': 50, 'category': clothing},
    {'name': 'Jeans', 'price': 49.99, 'description': 'Blue denim jeans', 'count': 30, 'category': clothing},
    {'name': 'Jacket', 'price': 79.99, 'description': 'Winter jacket', 'count': 20, 'category': clothing},
    {'name': 'Sneakers', 'price': 89.99, 'description': 'Running sneakers', 'count': 25, 'category': clothing},
    {'name': 'Hat', 'price': 14.99, 'description': 'Baseball cap', 'count': 40, 'category': clothing},

    # Books
    {'name': 'Python Guide', 'price': 29.99, 'description': 'Complete Python programming guide', 'count': 15, 'category': books},
    {'name': 'Django Handbook', 'price': 34.99, 'description': 'Django web development', 'count': 10, 'category': books},
    {'name': 'Fiction Novel', 'price': 19.99, 'description': 'Bestselling fiction', 'count': 20, 'category': books},
    {'name': 'Cookbook', 'price': 24.99, 'description': 'International recipes', 'count': 12, 'category': books},
    {'name': 'Biography', 'price': 22.99, 'description': 'Famous person biography', 'count': 8, 'category': books},

    # Home & Garden
    {'name': 'Chair', 'price': 149.99, 'description': 'Comfortable office chair', 'count': 10, 'category': home_garden},
    {'name': 'Table', 'price': 299.99, 'description': 'Dining table', 'count': 5, 'category': home_garden},
    {'name': 'Lamp', 'price': 39.99, 'description': 'Desk lamp', 'count': 18, 'category': home_garden},
    {'name': 'Plant', 'price': 24.99, 'description': 'Indoor plant', 'count': 22, 'category': home_garden},
    {'name': 'Cushion', 'price': 19.99, 'description': 'Decorative cushion', 'count': 30, 'category': home_garden},
]

for prod_data in products:
    Product.objects.get_or_create(**prod_data)

print("Data populated successfully!")