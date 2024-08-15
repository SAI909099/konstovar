from django.shortcuts import render
from django.views.generic import ListView, DetailView

from apps.models import Product, Category


def my_view(request):
    return render(request, 'apps/2_index.html')


class ProductListView(ListView):
    queryset = Product.objects.order_by('-created_at')
    template_name = 'apps/2_index.html'
    paginate_by = 5
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['categories'] = Category.objects.all()
        return data


class ProductDetailView(DetailView):
    model = Product
    template_name = 'order/product_detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['categories'] = Category.objects.all()
        return data