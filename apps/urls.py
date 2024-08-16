from django.urls import path

from .views import ProductList, CategoryView

urlpatterns = [
    path('', ProductList.as_view(), name='home_page'),
    path('market/<slug:foo>/', CategoryView.as_view(), name='category_page'),
]
