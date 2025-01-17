// Seletores gerais
document.addEventListener('DOMContentLoaded', function () {
    atualizarTotal(); // Chama a função quando a página é carregada
});
const sidebarLinks = document.querySelectorAll('#sidebarMenu a');
const sidebarMenu = document.getElementById('sidebarMenu');
const counterElement = document.getElementById('counter'); // Contador de quantidade
const precoElemento = document.getElementById('preco-produto'); // Preço do produto
const totalElemento = document.getElementById('total'); // Total
const tabelaCorpo = document.getElementById("tabela-corpo");

var staticURL = typeof staticURL !== 'undefined' ? staticURL : "/static/";

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

    // Determinar a imagem com base na categoria
    let imagemSrc;
    switch (produtoCategoria) {
        case "Smartphones":
            imagemSrc = staticPath + "SMARTPHONES.png";
            break;
        case "Computadores e Notebooks":
            imagemSrc = staticPath + "COMPUTADORES.png";
            break;
        case "TVs":
            imagemSrc = staticPath + "TVS.png";
            break;
        case "Áudio e Som":
            imagemSrc = staticPath + "SOM.png";
            break;
        case "Games e Consoles":
            imagemSrc = staticPath + "CONSOLE.png";
            break;
        case "Eletrodomésticos Portáteis":
            imagemSrc = staticPath + "ELETROPORTATEIS.png";
            break;
        case "Acessórios":
            imagemSrc = staticPath + "ACESSORIOS.png";
            break;
        case "Câmeras e Fotografia":
            imagemSrc = staticPath + "CAMERAS.png";
            break;
        case "Automação Residencial":
            imagemSrc = staticPath + "AUTOMACAO.png";
            break;
        case "Componentes e Periféricos":
            imagemSrc = staticPath + "PERIFERICOS.png";
            break;
        case "Redes e Conectividade":
            imagemSrc = staticPath + "REDES.png";
            break;
        case "Energia e Carregamento":
            imagemSrc = staticPath + "ENERGIA.png";
            break;
        default:
            imagemSrc = staticPath + "DEFAULT.png"; // Imagem padrão para categorias não listadas
    }

     // Criar a nova linha
     const novaLinha = document.createElement("tr");
     novaLinha.innerHTML = `
         <td>
             <h2>${produtoCategoria}</h2>
             <img src="${imagemSrc}" alt="${produtoCategoria}" style="width: 50px; height: 50px;" />
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
             <h2 id="preco-produto">R$ ${produtoPreco.toFixed(2)}</h2>
         </td>
         <td>
            <button onclick="removerLinha(this)" class="btn btn-danger mt-4" >Remover</button>
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
    let total = 0;
    const linhas = document.querySelectorAll('#tabela-corpo tr');

    linhas.forEach(linha => {
        const precoElemento = linha.querySelector('#preco-produto');
        const quantidadeElemento = linha.querySelector('.counter');

        if (precoElemento && quantidadeElemento) {
            const preco = parseFloat(precoElemento.textContent.replace('R$', '').replace(',', '.'));
            const quantidade = parseInt(quantidadeElemento.textContent);
            total += preco * quantidade;
        }
    });

    // Atualiza o total na tela
    const totalElemento = document.getElementById('total');
    totalElemento.textContent = `R$${total.toFixed(2).replace('.', ',')}`;
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
    let quantidade = parseInt(counter.textContent || 0);
    
    if (quantidade > 0) {
        quantidade -= 1; // Decrementa
        counter.textContent = quantidade;
    } else {
        alert('A quantidade não pode ser menor que zero!');
    }

    atualizarTotal();
}

// Menu lateral: Mostrar/ocultar animação
sidebarMenu.addEventListener('show.bs.collapse', () => {
    sidebarMenu.style.transition = 'all 0.5s ease-in-out';
});

function removerLinha(botao) {
    const linha = botao.closest('tr'); // Encontra a linha correspondente
    
    // Confirmação antes de remover
    if (confirm("Você tem certeza que deseja remover este produto?")) {
        linha.remove(); // Remove a linha
        atualizarTotal(); // Atualiza o total após a remoção
    }
}

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