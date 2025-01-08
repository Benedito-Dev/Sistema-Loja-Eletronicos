from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('produtos/', views.produtos, name='produtos'),
    path('produtos/listar', views.listar_produtos, name='listar_produtos'),
    path('vendas/', views.vendas, name='vendas'),
    path('vendas/registrar/', views.registrar_venda, name='registrar_venda'),   # Subpágina Registrar Venda
    path('relatorios/', views.relatorios, name='relatorios'),
    path('funcionarios/', views.funcionarios, name='funcionarios'),
    path('config/', views.configuracoes, name='configuracoes'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),  # Redireciona para a página de login após o logout
]