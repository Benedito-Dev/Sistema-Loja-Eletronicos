// Seletores gerais
const sidebarLinks = document.querySelectorAll('#sidebarMenu a');
const sidebarMenu = document.getElementById('sidebarMenu');
const counterElement = document.getElementById('counter'); // Contador de quantidade
const precoElemento = document.getElementById('preco-produto'); // Preço do produto
const totalElemento = document.getElementById('total'); // Total
const tabelaCorpo = document.getElementById("tabela-corpo");

// Evento: Seleção de categoria
 function adicionarProduto() {
    // Obtendo url da pasta static
    const staticPath = staticURL + "img/categorias/"

     // Obter o elemento <select> e a opção selecionada
     const select = document.getElementById("categoria");
     const selectedOption = select.options[select.selectedIndex];

     // Verifica se uma opção válida foi selecionada
     if (selectedOption.value === "") {
         alert("Por favor, selecione um produto.");
         return;
     }

     // Dados do produto selecionado
     const produtoId = selectedOption.value;
     const produtoNome = selectedOption.getAttribute("data-nome");
     const produtoPreco = parseFloat(selectedOption.getAttribute("data-preco"));
     const produtoCategoria = selectedOption.getAttribute("data-categoria");

     // Criar a nova linha
     const novaLinha = document.createElement("tr");
     novaLinha.innerHTML = `
         <td>
             <h2>${produtoCategoria}</h2>
             <img src="${staticPath + "SMARTPHONES.png"}" alt="${produtoCategoria}" style="width: 50px; height: 50px;" />
         </td>
         <td>
             <h2>${produtoNome}</h2>
         </td>
         <td>
             <div class="item-quant">
                 <button class="minus" onclick="decrement(this)">-</button>
                 <div class="counter">1</div>
                 <button class="plus" onclick="increment(this)">+</button>
             </div>
         </td>
         <td>
             <h2 class="preco-produto">R$ ${produtoPreco.toFixed(2)}</h2>
         </td>
     `;

     // Adicionar a nova linha na tabela
     document.getElementById("tabela-corpo").appendChild(novaLinha);

     // Atualizar o total
     atualizarTotal();

     // Limpar a seleção do <select>
     select.value = "";
 }


// Função para atualizar o total
function atualizarTotal() {
    const quantidade = parseInt(counterElement.textContent); // Obtém a quantidade do contador
    const preco = parseFloat(precoElemento.textContent.replace('R$', '').replace(',', '').replace('.', '.')); // Converte o preço para número
    const total = preco * quantidade; // Calcula o total
    totalElemento.textContent = `R$ ${total.toLocaleString('pt-BR', { minimumFractionDigits: 2 })}`; // Atualiza o total formatado
}

// Função para incrementar a quantidade
function increment(button) {
    const counter = button.parentElement.querySelector('.counter');
    let quantidade = parseInt(counter.textContent);
    quantidade += 1; // Incrementa
    counter.textContent = quantidade;
    atualizarTotal();
}

// Função para decrementar a quantidade
function decrement(button) {
    const counter = button.parentElement.querySelector('.counter');
    let quantidade = parseInt(counter.textContent);
    if (quantidade > 1) {
        quantidade -= 1; // Decrementa
        counter.textContent = quantidade;
        atualizarTotal();
    }
}

// Menu lateral: Mostrar/ocultar animação
sidebarMenu.addEventListener('show.bs.collapse', () => {
    sidebarMenu.style.transition = 'all 0.5s ease-in-out';
});

// Evento: Clique nos links do menu lateral
sidebarLinks.forEach(link => {
    link.addEventListener('click', () => {
        // Remove a classe "active" de todos os links
        sidebarLinks.forEach(l => l.classList.remove('active'));
        link.classList.add('active');

        // Adiciona "active" na opção principal se for subopção
        const parentDropdown = link.closest('.dropdown');
        if (parentDropdown) {
            const parentLink = parentDropdown.querySelector('a');
            parentLink.classList.add('active');
        }
    });
});