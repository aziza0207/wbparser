from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "price",
        "discounted_price",
        "rating",
        "review_count",
        "created_at",
    )
    list_filter  = ("rating", "review_count",)
    search_fields = ("title",)
    ordering = ("-created_at",)
