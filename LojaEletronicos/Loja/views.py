from django.shortcuts import render, redirect # type: ignore
from .models import Produto
from django.contrib.auth import authenticate, login, get_user_model # type: ignore # Funções para autenticação e login
from django.contrib.auth.decorators import login_required # type: ignore
from django.contrib import messages
from django.contrib.auth.models import User
 # type: ignore # Para mensagens de erro ou sucesso

def login_view(request):
    
    if request.method == "POST":
        email = request.POST.get("email").strip()
        password = request.POST.get("password")

        # Remove espaços em branco extras
        User = get_user_model()
        #user = User.objects.get(email)

        # Teste para recebimento de dados
        print(f"Email recebido: '{email}', senha recebida: '{password}'")

        try:
            # Verificar se o usuário existe pelo email (Django usa username por padrão)
            #from django.contrib.auth.models import User # type: ignore
            User = get_user_model()
            user = User.objects.get(email=email)#            user = User.objects.get(email=email)
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
    user = get_user_model
    nome = request.user.first_name
    return render(request, 'home/home.html', {"nome": nome})

@login_required
def produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/produtos.html', {'produtos' : produtos})

@login_required
def vendas(request):
    return render(request, 'vendas/vendas.html')

@login_required
def relatorios(request):
    # if not request.user.is_authenticated:
    #     messages.error(request, "Você precisa estar logado para acessar esta página.")
    #     return redirect('')
    return render(request, 'relatorios/relatorios.html')

@login_required
def funcionarios(request):
    # if not request.user.is_authenticated:
    #     messages.error(request, "Você precisa estar logado para acessar esta página.")
    #     return redirect('')
    return render(request, 'funcionarios/funcionarios.html')

@login_required
def configuracoes(request):
    # if not request.user.is_authenticated:
    #     messages.error(request, "Você precisa estar logado para acessar esta página.")
    #     return redirect('')
    return render(request, 'configuracoes.html')


# SubPaginas

@login_required
def registrar_venda(request):
    # if not request.user.is_authenticated:
    #     messages.error(request, "Você precisa estar logado para acessar esta página.")
    return render(request, 'vendas/registrar_venda.html')

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listar_produto.html', {'produtos' : produtos})

def adicionar_produtos(request):
    referer = request.META.get('HTTP_REFERER')  # Obtém a URL de onde o usuário veio
    mostrar_botao = False
    
    if referer and 'produtos/listar' in referer:  # Substitua 'pagina-especifica' pela URL ou parte dela
        mostrar_botao = True

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
        return redirect('listar_produtos')  # Redireciona para a lista de produtos

    return render(request, 'produtos/adicionar_produtos.html', {'mostrar_botao': mostrar_botao})

def excluir_produtos(request):
    if request.method == 'POST':
        # Capturar os IDs dos produtos selecionados
        produtos_selecionados = request.POST.getlist('produtos_selecionados')
        print(produtos_selecionados)
        # if produtos_selecionados:
        #     # Excluir os produtos selecionados
        #     Produto.objects.filter(id__in=produtos_selecionados).delete()
        #     messages.success(request, 'Produtos excluídos com sucesso!')
        # else:
        #     messages.error(request, 'Nenhum produto foi selecionado.')
    return redirect('listar_produtos')  # Substitua pelo nome da página onde está o formulário


def editar_funcionario(request):
    # User = get_user_model
    funcionarios = get_user_model().objects.all()
    return render(request,'funcionarios/editar_funcionario.html', {'funcionarios': funcionarios})

def adicionar_funcionario(request):
    if request.method == "POST":
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        endereco = request.POST['endereco']
        salario = request.POST['salario']
        telefone = request.POST['telefone']
        cargo = request.POST['cargo']
        User = get_user_model()
        
        User.objects.create(
            username=nome,
            email=email,
            password=senha,
            endereco=endereco,
            salario=salario,
            telefone=telefone,
            cargo=cargo
        )   
        User.set_password(senha)
        User.save()
    return render(request, 'funcionarios/adicionar_funcionario.html')

def excluir_funcionario(request):
    if request.method == 'POST':
        User = get_user_model()
        # Capturar os IDs dos produtos selecionados
        produtos_selecionados = request.POST.getlist('funcionarios_selecionados')
        if produtos_selecionados:
             # Excluir os produtos selecionados
             User.objects.filter(id__in=produtos_selecionados).delete()
             messages.success(request, 'Produtos excluídos com sucesso!')
        else:
             messages.error(request, 'Nenhum produto foi selecionado.')
    return redirect('editar_funcionario')  # Substitua pelo nome da página onde está o formulário