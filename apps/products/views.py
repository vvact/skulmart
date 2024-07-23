from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



# @api_view(['GET'])
# def getProductBySlug(request, slug):
#     product = get_object_or_404(Product, slug=slug)
#     serializer = ProductSerializer(product, many=False)
#     return Response(serializer.data)