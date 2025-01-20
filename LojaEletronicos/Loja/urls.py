from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('produtos/', views.produtos, name='produtos'),
    path('produtos/listar', views.listar_produtos, name='listar_produtos'),
    path('produtos/adicionar', views.adicionar_produtos, name='adicionar_produtos'),
    path('produtos/excluir', views.excluir_produtos, name='excluir_produtos'),
    path('vendas/', views.vendas, name='vendas'),
    path('vendas/registrar/', views.registrar_venda, name='registrar_venda'),   # Subpágina Registrar Venda
    path('relatorios/', views.relatorios, name='relatorios'),
    path('funcionarios/', views.funcionarios, name='funcionarios'),
    path('config/', views.configuracoes, name='configuracoes'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),  # Redireciona para a página de login após o logout
    path('funcionario/gerenciar', views.gerenciar_funcionario, name='gerenciar_funcionario'),
    path('funcionarios/listar', views.listar_funcionario, name='listar_funcionarios'),
    path('funcionario/cadastrar', views.adicionar_funcionario, name='adicionar_funcionario'),
    path('funcionario/excluir', views.excluir_funcionario, name='excluir_funcionario'),
    path('funcionario/editar-funcionario/<int:funcionario_id>/', views.editar_funcionario, name='editar_funcionario'),
]