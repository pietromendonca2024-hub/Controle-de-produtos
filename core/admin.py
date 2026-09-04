from django.contrib import admin
from .models import Brand, Category, Product

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active','description')
    list_filter = ('is_active',)
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active','description')
    list_filter = ('is_active',)
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'price', 'is_active','description')
    list_filter = ('brand', 'category', 'is_active',)
    search_fields = ('name',)
