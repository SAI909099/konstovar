from django.urls import path

from .views import ProductList, CategoryView, OKompanyView, CompanyContactsView, ManufactureView

urlpatterns = [
    path('', ProductList.as_view(), name='home_page'),
    path('market/<slug:slug>/', CategoryView.as_view(), name='category_page'),
    path('o-kompani/', OKompanyView.as_view(), name='o-kompany'),
    path('kontakty', CompanyContactsView.as_view(), name='kontakt'),
    path('proizvoditeli/', ManufactureView.as_view(), name='proizvaditeli'),

]
