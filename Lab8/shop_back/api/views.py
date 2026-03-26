from django.http import JsonResponse

from .models import Category, Product


def product_to_dict(product):
    return {
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "description": product.description,
        "count": product.count,
        "is_active": product.is_active,
        "category": {
            "id": product.category.id,
            "name": product.category.name,
        },
    }


def category(request, id=None):
    if id:
        category = Category.objects.get(pk=id)
        return JsonResponse({"id": category.id, "name": category.name})

    categories = list(Category.objects.values("id", "name"))
    return JsonResponse(categories, safe=False)


def category_products(request, id):
    products = [
        product_to_dict(product)
        for product in Product.objects.all()
        if product.category.name.lower() == Category.objects.get(pk=id).name.lower()
    ]

    return JsonResponse(products, safe=False)


def product(request, id=None, category_name=None):
    if id:
        product = Product.objects.get(pk=id)
        return JsonResponse(product_to_dict(product))

    products = [product_to_dict(product) for product in Product.objects.all()]

    if category_name:
        filtered_products = [
            product
            for product in products
            if product["category"]["name"].lower() == category_name.lower()
        ]
        products = filtered_products

    return JsonResponse(products, safe=False)
