from django.contrib.admin import ModelAdmin, register, StackedInline
from mptt.admin import DraggableMPTTAdmin

from apps.models import Product, Category, Tag, ImageProduct


@register(Category)
class CategoryModelAdmin(DraggableMPTTAdmin):
    pass


class ProductImageStackedInline(StackedInline):
    model = ImageProduct
    extra = 1
    min_num = 0
    max_num = 5
@register(Product)
class ProductModelAdmin(ModelAdmin):
    list_display = ('id', 'name', 'category_id')
    inlines = [ProductImageStackedInline]


@register(Tag)
class TagModelAdin(ModelAdmin):
    pass
