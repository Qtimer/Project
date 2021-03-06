from django.contrib import admin

# Register your models here.
from apps.products.models import Product, ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product_status', 'date_of_sale', 'seller', 'price', 'freight_fee', 'freight')
    search_fields = ['id', 'name', 'seller__phone_number']
    list_filter = ['product_status']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'sequence', 'image_tag')
