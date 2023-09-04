from django.urls import path
from .views import home, save
from django.conf.urls.static import static

urlpatterns = [
    path('', home),
    path('save/', save, name="save"),
]