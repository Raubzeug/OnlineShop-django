from django.contrib import admin

from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def desc_short(self, obj: Product):
        if len(obj.description) < 30:
            return obj.description
        else:
            return f'{obj.description[:30]}...'
    list_display = ['id', 'title', 'price', 'type', 'desc_short']
    list_editable = ['title', 'price']
