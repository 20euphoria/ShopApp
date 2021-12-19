from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "product_id", "name", "weight", "price", "created_at", "updated_at"
        ]
