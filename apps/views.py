from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from apps.models import Product, Category


class ProductList(ListView):
    queryset = Product.objects.order_by('-created_at')
    template_name = 'apps/home_page.html'
    paginate_by = 5
    context_object_name = "products"



class CategoryView(ListView):
    template_name = 'apps/category_product_list.html'
    model = Category
    context_object_name = 'products'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['foo'])
        return Product.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context