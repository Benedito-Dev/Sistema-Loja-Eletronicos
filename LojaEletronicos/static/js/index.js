const email = document.getElementById('email')
const senha = document.getElementById('senha')
const login = document.getElementById('logar')
const exibirSenhaCheckbox = document.getElementById('exibirSenha');

exibirSenhaCheckbox.addEventListener('change', function() {
    if (exibirSenhaCheckbox.checked) {
        senha.type = 'text';  // Exibir senha
    } else {
        senha.type = 'password';  // Ocultar senha
    }
});