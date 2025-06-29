from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from .models import Product
from .serializers import ProductSerializer
from drf_spectacular.utils import  OpenApiParameter, OpenApiTypes
from drf_spectacular.utils import extend_schema_view, extend_schema
from .filters import ProductFilter

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends  = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ProductFilter
