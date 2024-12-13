const email = document.getElementById('email')
const senha = document.getElementById('senha')
const login = document.getElementById('logar')
const exibirSenhaCheckbox = document.getElementById('exibirSenha');

login.addEventListener("click", function () {
    // Verifica se o email ou a senha estão vazios
    if (email.value.trim() === "" || senha.value.trim() === "") {
        alert("Por favor, preencha ambos os campos (email e senha).");
    } else {
        alert(`Você clicou no botão! Email: ${email.value}`);
    }
});

exibirSenhaCheckbox.addEventListener('change', function() {
    if (exibirSenhaCheckbox.checked) {
        senha.type = 'text';  // Exibir senha
    } else {
        senha.type = 'password';  // Ocultar senha
    }
});