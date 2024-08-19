from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View

from apps.models import Product, Category, Cart

from django.views.generic import ListView, TemplateView, DetailView, CreateView


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'apps/home_page.html'

    def queryset(self):
        category_slug = self.request.GET.get('category_slug')
        if category_slug:
            return Product.objects.filter(category__slug=category_slug)
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        selected_category = self.request.GET.get('category')
        context['categories'] = categories
        context['selected_category'] = selected_category
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'order/product_detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'

    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     data['categories'] = Category.objects.all()
    #     return data


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


class MagazineCartView(TemplateView):
    template_name = 'apps/magazine_cart.html'


class CartSaveView(View):
    def post(self, request, *args, **kwargs):
        product = Product.objects.get(slug=self.kwargs['slug'])
        obj, created = Cart.objects.get_or_create(user=request.user, product=product)
        if not created:
            obj.delete()
            return JsonResponse({'save': 0})
        return JsonResponse({'save': 1})
