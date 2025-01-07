from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('produtos/', views.produtos, name='produtos'),
    path('produtos/estoque/', views.listar_produtos, name='lista_produtos'),
    # path('produtos/estoque/adicionar', views.adicionar_produtos, name='Adicionar produtos'),
    path('vendas/', views.vendas, name='vendas'),
    path('vendas/registrar/', views.registrar_venda, name='registrar_venda'),   # Subpágina Registrar Venda
    path('relatorios/', views.relatorios, name='relatorios'),
    path('funcionarios/', views.funcionarios, name='funcionarios'),
    path('config/', views.configuracoes, name='configuracoes'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),  # Redireciona para a página de login após o logout
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)