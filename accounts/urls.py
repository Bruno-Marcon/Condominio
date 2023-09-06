from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name = 'Condominio/accounts/templates/login/login.html'
        ), name="login"),
]