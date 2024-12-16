from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages  

def login(request):
    if request.method == "POST":  # Apenas processa o login se for uma requisição POST
        email = request.POST.get("email")  # Obtém o email do formulário enviado
        password = request.POST.get("password")  # Obtém a senha do formulário enviado

        # Teste para recebimento de dados
        print(f"Email recebido: '{email}', senha recebida: '{password}'")

        # Remove espaços em branco extras
        email = email.strip()

        try:
            # Verificar no banco de dados se o email existe
            user = User.objects.get(email=email)
            print(f"Usuário encontrado: {user}")

            # Verificar se a senha está correta
            if user.check_password(password):
                # Caso as credenciais sejam válidas
                messages.success(request, "Login bem-sucedido!")
                return redirect('home')  # Redireciona para a página inicial ou outra página
            else:
                # Caso a senha esteja incorreta
                messages.error(request, "Senha inválida!")
        except User.DoesNotExist:
            # Caso o email não exista no banco de dados
            print(f"Usuário com o email '{email}' não encontrado no banco de dados.")
            messages.error(request, "Usuário não encontrado!")

    # Caso não seja uma requisição POST ou tenha falhado o login
    return render(request, 'login.html')  # Retorna à página de login

def home(request):
    return render(request, 'home.html')
