const sidebarLinks = document.querySelectorAll('#sidebarMenu a');
const sidebarMenu = document.getElementById('sidebarMenu');
const counterElement = document.getElementById('counter'); // Contador de quantidade
const precoElemento = document.getElementById('preco-produto'); // Preço do produto
const totalElemento = document.getElementById('total'); // Total

// Converte o preço do produto para número
const preco = parseFloat(precoElemento.textContent.replace('R$', '').replace(',', '').replace('.', '.')); // Retira "R$" e formata

// Função para atualizar o total
function atualizarTotal() {
    const quantidade = parseInt(counterElement.textContent); // Obtém a quantidade do contador
    const total = preco * quantidade; // Multiplica o preço pela quantidade
    totalElemento.textContent = `R$ ${total.toLocaleString('pt-BR', { minimumFractionDigits: 2 })}`; // Atualiza o total no formato correto
}

// Função para incrementar a quantidade
function increment() {
    let quantidade = parseInt(counterElement.textContent); // Obtém a quantidade atual
    quantidade += 1; // Incrementa a quantidade
    counterElement.textContent = quantidade; // Atualiza o contador
    atualizarTotal(); // Recalcula o total
}

// Função para decrementar a quantidade
function decrement() {
    let quantidade = parseInt(counterElement.textContent); // Obtém a quantidade atual
    if (quantidade > 1) { // Garante que a quantidade não seja menor que 1
        quantidade -= 1; // Decrementa a quantidade
        counterElement.textContent = quantidade; // Atualiza o contador
        atualizarTotal(); // Recalcula o total
    }
}

sidebarMenu.addEventListener('show.bs.collapse', () => {
        sidebarMenu.style.transition = 'all 0.5s ease-in-out';
    });

    // Adiciona um evento de clique para cada link
    sidebarLinks.forEach(link => {
        link.addEventListener('click', () => {

            // Remove a classe "active" de todos os links
            sidebarLinks.forEach(l => l.classList.remove('active'));

            // Adiciona a classe "active" ao link clicado
            link.classList.add('active');

            // Caso o link clicado seja uma subopção, adiciona "active" na opção principal
            const parentDropdown = link.closest('.dropdown');
            if (parentDropdown) {
                const parentLink = parentDropdown.querySelector('a');
                parentLink.classList.add('active');
            }
        });
    });
