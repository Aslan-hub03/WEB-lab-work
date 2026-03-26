from django.urls import path

from . import views

urlpatterns = [
    path("categories/", views.category),
    path("categories/<int:id>", views.category),
    path("categories/<int:id>/products", views.category_products),
    path("products/", views.product),
    path("products/<int:id>", views.product),
]
