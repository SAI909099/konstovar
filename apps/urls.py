from django.conf.urls.static import static
from django.urls import path

from root import settings
from . import views
from .views import HomepageTemplateView

urlpatterns = [
    path('', HomepageTemplateView.as_view(), name='home_page'),

]
