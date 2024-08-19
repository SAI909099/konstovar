from django.urls import path

# from .views import ProductList, CategoryView, OKompanyView, CompanyContactsView, ManufactureView
from .views import ProductListView, ProductDetailView, CategoryView, OKompanyView, CompanyContactsView, ManufactureView, \
    MagazineCartView, CartSaveView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list_page'),
    path('product/list', ProductListView.as_view(), name='product_list'),
    # path('product/detail/<str:slug>', ProductDetailView.as_view(), name='product_detail'),
    # path('', ProductListView.as_view(), name='home_page'),
    path('market/<slug:slug>/', CategoryView.as_view(), name='category_page'),
    path('o-kompani/', OKompanyView.as_view(), name='o-kompany'),
    path('kontakty', CompanyContactsView.as_view(), name='kontakt'),
    path('proizvoditeli/', ManufactureView.as_view(), name='proizvaditeli'),

]
urlpatterns += [
    path('magazine/cart', MagazineCartView.as_view(), name='magazine_cart'),
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/detail/<str:slug>', ProductDetailView.as_view(), name='product_detail'),
    path('product/cart/<str:slug>', CartSaveView.as_view(), name='cart_save'),
]
