from django.contrib import admin
from .models import Category, Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'series', 'price', 'stock_quantity', 'stock_status')
    list_filter = ('category', 'stock_status')
    search_fields = ('name', 'series')
    readonly_fields = ('stock_status',)
    inlines = [ProductImageInline]