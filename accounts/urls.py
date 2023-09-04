from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('register/',views.SignUp.as_view(), name="signUp"), 
]