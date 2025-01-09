from django.shortcuts import render, redirect
from .models import Produto
from django.contrib.auth import authenticate, login  # Funções para autenticação e login
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Para mensagens de erro ou sucesso

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Remove espaços em branco extras
        email = email.strip()

        # Teste para recebimento de dados
        print(f"Email recebido: '{email}', senha recebida: '{password}'")

        try:
            # Verificar se o usuário existe pelo email (Django usa username por padrão)
            from django.contrib.auth.models import User
            user = User.objects.get(email=email)
            print(f"Usuário encontrado: {user}")

            # Autenticar o usuário usando username e senha
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                # Login do usuário (criação da sessão)
                login(request, user)
                messages.success(request, "")
                return redirect('home')  # Redireciona para a home
            else:
                messages.error(request, "Senha inválida!")
        except User.DoesNotExist:
            messages.error(request, "Usuário com este email não foi encontrado.")

    return render(request, 'login/login.html')

@login_required
def home(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para acessar esta página.")
        return redirect('')
    return render(request, 'home/home.html')

@login_required
def produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/produtos.html', {'produtos' : produtos})

@login_required
def vendas(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para acessar esta página.")
        return redirect('')
    return render(request, 'vendas/vendas.html')

@login_required
def relatorios(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para acessar esta página.")
        return redirect('')
    return render(request, 'relatorios/relatorios.html')

@login_required
def funcionarios(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para acessar esta página.")
        return redirect('')
    return render(request, 'funcionarios/funcionarios.html')

@login_required
def configuracoes(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para acessar esta página.")
        return redirect('')
    return render(request, 'configuracoes.html')


# SubPaginas

@login_required
def registrar_venda(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para acessar esta página.")
    return render(request, 'vendas/registrar_venda.html')

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listar_produto.html', {'produtos' : produtos})


def adicionar_produtos(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        preco = request.POST['preco']
        quant = request.POST['quant']
        categoria = request.POST['categoria']
        marca = request.POST['marca']

        Produto.objects.create(
            nome=nome,
            preco=preco,
            quant=quant,
            categoria=categoria,
            marca=marca
        )
        return redirect('home')  # Redireciona para a lista de produtos

    return render(request, 'produtos/adicionar_produtos.html')