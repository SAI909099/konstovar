from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView

from apps.models import Product, Category


class ProductList(ListView):
    queryset = Product.objects.order_by('-created_at')
    template_name = 'apps/home_page.html'
    paginate_by = 5
    context_object_name = "products"

class OKompanyView(TemplateView):
    template_name = 'from_company/from_company.html'

class CompanyContactsView(TemplateView):
    template_name = 'from_company/contact.html'

class ManufactureView(TemplateView):
    template_name = 'from_company/manufacturers.html'

class DeliveryView(TemplateView):
    template_name = 'delivery/deleveriy.html'

class CategoryView(ListView):
    template_name = 'apps/category_product_list.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        # Retrieve the category based on the slug passed in the URL
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        # Filter products by this category
        return Product.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        # Get the base context from ListView
        context = super().get_context_data(**kwargs)
        # Add the category to the context
        context['category'] = self.category
        # Add the category's children to the context
        context['children'] = self.category.get_children()
        return context



# from django.shortcuts import render, get_object_or_404
# from .models import Category
#
#
# def category_detail(request, slug):
#     # Retrieve the category based on the slug
#     category = get_object_or_404(Category, slug=slug)
#     # Get all children of the category
#     children = category.get_children()
#
#     # Pass the category and its children to the template
#     context = {
#         'category': category,
#         'children': children,
#     }
#     return render(request, 'category_detail.html', context)
