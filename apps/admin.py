from django.contrib import admin
from django.contrib.admin import ModelAdmin, register

from apps.models import Product


@register(Product)
class ProductModelAdmin(ModelAdmin):
    list_display = ('id', 'name', 'category_id')


    def parent_category(self, obj):
        return obj.category_id.parent_id if obj.category_id and obj.category_id.parent_id else None
