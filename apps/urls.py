from django.conf.urls.static import static
from django.urls import path

from root import settings
from . import views

urlpatterns = [
    path('', views.my_view, name='home'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)

