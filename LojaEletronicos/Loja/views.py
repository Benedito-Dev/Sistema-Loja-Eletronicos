from django.shortcuts import render, redirect # type: ignore
from .models import Produto
from django.contrib.auth import authenticate, login  # type: ignore # Funções para autenticação e login
from django.contrib.auth.decorators import login_required # type: ignore
from django.contrib import messages  # type: ignore # Para mensagens de erro ou sucesso

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
            from django.contrib.auth.models import User # type: ignore
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
    nome = request.user.first_name
    return render(request, 'home/home.html', {"nome": nome})

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
def gerenciar_produtos(request):
    if request.method == "POST":
        produtos_selecionados = request.POST.getlist("produtos_selecionados")
        acao = request.POST.get("acao")

        if not produtos_selecionados:
            messages.error(request, "Selecione pelo menos um produto.")
            return redirect("listar_produtos")

        if acao == "excluir":
            # Lógica para excluir produtos
            for produto_id in produtos_selecionados:
                # Exclua o produto usando o ID
                Produto.objects.filter(id=produto_id).delete()
            return redirect("listar_produtos")
        
        elif acao == "vender":
            # Lógica para redirecionar para a página de vendas com os produtos selecionados
            request.session["produtos_para_venda"] = produtos_selecionados
            return redirect("registrar_venda")

    return redirect("listar_produtos")

@login_required
def registrar_venda(request):
    # Recupera os produtos da sessão
    produtos_selecionados = request.session.get("produtos_para_venda", [])

    # Verifica se há produtos selecionados
    if not produtos_selecionados:
        messages.error(request, "Nenhum produto selecionado para venda.")
        return redirect("listar_produtos")

    # Busca os objetos Produto correspondentes aos IDs
    produtos = Produto.objects.filter(id__in=produtos_selecionados)

    # Passa os produtos para o template
    return render(request, 'vendas/registrar_venda.html', {'produtos': produtos})

@login_required
def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listar_produto.html', {'produtos' : produtos})

@login_required
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

@login_required
def excluir_produtos(request):
    if request.method == 'POST':
        # Capturar os IDs dos produtos selecionados
        produtos_selecionados = request.POST.getlist('produtos_selecionados')
        print(produtos_selecionados)  # Verificando os produtos selecionados

        if produtos_selecionados:
            # Excluir os produtos selecionados
            Produto.objects.filter(id__in=produtos_selecionados).delete()

    return redirect('listar_produtos')  # Redireciona para a página inicial (ou outra página de sua escolha)