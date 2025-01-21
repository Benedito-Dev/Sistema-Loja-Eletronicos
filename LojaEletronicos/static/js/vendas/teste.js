// Instanciando Variáveis
const linhas = document.querySelectorAll('#tabela-corpo tr');

// Função para atualizar os subtotais e o total
function atualizarValores() {
    let totalProdutos = 0;

    // Itera sobre cada linha de produto
    document.querySelectorAll('tbody tr').forEach(function (linha) {
        const precoElement = linha.querySelector('.price');
        const quantidadeElement = linha.querySelector('.counter');
        const subtotalElement = linha.querySelector('.subtotal');

        const preco = parseFloat(precoElement.textContent.replace('R$', '').replace(',', '.'));
        const quantidade = parseInt(quantidadeElement.textContent);

        if (!isNaN(preco) && !isNaN(quantidade)) {
            const subtotal = preco * quantidade;
            subtotalElement.textContent = `R$${subtotal.toFixed(2)}`;
            totalProdutos += subtotal;
        }
    });

    // Atualiza o total dos produtos no resumo
    const totalElement = document.getElementById('total');
    totalElement.textContent = `R$${totalProdutos.toFixed(2)}`;
}

// Função para incrementar a quantidade
function increment(button) {
    const counterElement = button.parentElement.querySelector('.counter');
    let quantidade = parseInt(counterElement.textContent);
    counterElement.textContent = quantidade + 1;
    atualizarValores();
}

// Função para decrementar a quantidade
function decrement(button) {
    const counterElement = button.parentElement.querySelector('.counter');
    let quantidade = parseInt(counterElement.textContent);

    if (quantidade > 1) { // Evita que a quantidade fique abaixo de 1
        counterElement.textContent = quantidade - 1;
        atualizarValores();
    }
}

// Remover Produto
function removerLinha(botao) {
    const linha = botao.closest('tr'); // Encontra a linha correspondente
    
    // Confirmação antes de remover
    if (confirm("Você tem certeza que deseja remover este produto?")) {
        linha.remove(); // Remove a linha
        atualizarValores(); // Atualiza o total após a remoção
    }
}

// Adicionando listeners quando o DOM estiver carregado
document.addEventListener('DOMContentLoaded', function () {
    // Adiciona os event listeners para os botões de incrementar e decrementar
    document.querySelectorAll('.plus').forEach(function (button) {
        button.addEventListener('click', function () {
            increment(this);
        });
    });

    document.querySelectorAll('.minus').forEach(function (button) {
        button.addEventListener('click', function () {
            decrement(this);
        });
    });

    // Atualiza os valores na inicialização
    atualizarValores();
});
