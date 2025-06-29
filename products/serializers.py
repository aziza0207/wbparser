
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Product
        fields = ("wb_id", "title", "price",
                  "discounted_price", "rating", "review_count" )



