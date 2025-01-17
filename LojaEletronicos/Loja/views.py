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
        password = request.POST.get("password").strip()

        # Teste para recebimento de dados
        print(f"Email recebido: '{email}', senha recebida: '{password}'")

        User = get_user_model()

        try:
            # Buscar usuário pelo email
            user = User.objects.get(email=email)
            print(f"Usuário encontrado: {user}")

            # Autenticar usando o username e a senha
            authenticated_user = authenticate(request, username=user.username, password=password)
            print(authenticated_user)

            if authenticated_user is not None:
                # Fazer login
                login(request, authenticated_user)
                messages.success(request, "Login realizado com sucesso!")
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

def gerenciar_funcionario(request):
    if request.method == "POST":
        User = get_user_model()
        funcionarios_selecionados = request.POST.getlist('funcionarios_selecionados')
        acao = request.POST.get("acao")

        if not funcionarios_selecionados:
            messages.error(request, "Selecione pelo menos um funcionario.")
            return redirect("listar_funcionarios")

        if acao == "excluir":
            # Lógica para excluir produtos
            for funcionario_id in funcionarios_selecionados:
                # Exclua o produto usando o ID
                User.objects.filter(id=funcionario_id).delete()
            return redirect("listar_funcionarios")
        
        elif acao == "editar":
            # Lógica para redirecionar para a página de vendas com os produtos selecionados
            if len(funcionarios_selecionados) > 1:
                messages.error(request, "Selecione apenas um funcionario para editar.")

                return redirect("editar_funcionario", funcionario_id=funcionarios_selecionados[0])

    return redirect("listar_produtos")

def listar_funcionario(request):
    # User = get_user_model
    funcionarios = get_user_model().objects.all()
    return render(request,'funcionarios/listar_funcionario.html', {'funcionarios': funcionarios})

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
        
        user = User.objects.create(
            username=nome,
            email=email,
            password=senha,
            endereco=endereco,
            salario=salario,
            telefone=telefone,
            cargo=cargo
        )   
        user.set_password(senha)
        user.save()
    return render(request, 'funcionarios/adicionar_funcionario.html')

def excluir_funcionario(request):
    if request.method == 'POST':
        User = get_user_model()
        # Capturar os IDs dos produtos selecionados
        funcionarios_selecionados = request.POST.getlist('funcionarios_selecionados')
        if funcionarios_selecionados:
             User.objects.filter(id__in=funcionarios_selecionados).delete()
             messages.success(request, 'Funcionários excluídos com sucesso!')
        else:
             messages.error(request, 'Nenhum funcionário foi selecionado.')
    return redirect('editar_funcionario')  # Substitua pelo nome da página onde está o formulário

def editar_funcionario(request):
    if request.method == 'POST':
        User = get_user_model()
        # Capturar os IDs dos produtos selecionados
        funcionarios_selecionados = request.POST.getlist('funcionarios_selecionados')
        funcionario = User.objects.get(id=id)
       
        funcionario.nome = request.POST['nome']
        funcionario.email = request.POST['email']
        funcionario.endereco = request.POST['endereco']
        funcionario.salario = request.POST['salario']
        funcionario.telefone = request.POST['telefone']
        funcionario.cargo = request.POST['cargo']
        funcionario.save()
        
        messages.success(request, 'Funcionário editado com sucesso!')
        return redirect(request, 'listar_funcionario.html')

    return render(request, 'funcionarios/editar_funcionario.html', {'funcionarios': funcionarios})

