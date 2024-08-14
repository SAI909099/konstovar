from django.shortcuts import render
from django.views.generic import ListView

from apps.models import Product


def my_view(request):
    return render(request, 'apps/index.html')


class ProductListView(ListView):
    queryset = Product.objects.order_by('-created_at')
    template_name = 'apps/index.html'
    paginate_by = 5
    context_object_name = "products"
