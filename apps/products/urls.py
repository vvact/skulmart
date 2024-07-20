from django.urls import path,include
from rest_framework.routers import DefaultRouter
from. views import ProductViewSet
from .views import getProductBySlug

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/slug/<slug:slug>/', getProductBySlug, name='product-by-slug'),
    
]