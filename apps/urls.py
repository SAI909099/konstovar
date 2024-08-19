from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from root import settings
from . import views
from .views import HomepageTemplateView, RegisterFormView

urlpatterns = [
    path('', HomepageTemplateView.as_view(), name='home'),
    path('login/', LoginView.as_view(template_name='apps/auth/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='apps/auth/login.html'), name='logout'),
    path('register/', RegisterFormView.as_view(), name='register')
]
