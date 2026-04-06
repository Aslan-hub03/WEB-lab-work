from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Product
from api.serializers import ProductSerializer
from django.shortcuts import get_object_or_404


class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        return Response(ProductSerializer(products, many=True).data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ProductDetailAPIView(APIView):

    def get_object(self, product_id):
        return get_object_or_404(Product, id=product_id)

    def get(self, request, product_id):
        product = self.get_object(product_id)
        return Response(ProductSerializer(product).data)

    def put(self, request, product_id):
        product = self.get_object(product_id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, product_id):
        product = self.get_object(product_id)
        product.delete()
        return Response(status=204)