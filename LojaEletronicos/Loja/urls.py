from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('vendas/', views.vendas, name='vendas'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),  # Redireciona para a página de login após o logout
]