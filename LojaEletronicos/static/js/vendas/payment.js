document.addEventListener("DOMContentLoaded", function () {
    configurarSidebar();
    configurarPagamento();
});

// Configura os links da sidebar
function configurarSidebar() {
    const sidebarLinks = document.querySelectorAll('#sidebarMenu a');
    const sidebarMenu = document.getElementById('sidebarMenu');

    sidebarMenu.addEventListener('show.bs.collapse', () => {
        sidebarMenu.style.transition = 'all 0.5s ease-in-out';
    });

    sidebarLinks.forEach(link => {
        link.addEventListener('click', () => {
            sidebarLinks.forEach(l => l.classList.remove('active'));
            link.classList.add('active');
        });
    });
}

// Configurações de Pagamento
function configurarPagamento() {
    const pagamento = document.getElementById('tipo_de_pagamento');
    console.log(pagamento)
    if (!pagamento) return;

    if (pagamento.value === 'pix') {
        configurarPix();
    } else if (pagamento.value === 'cartao_credito') {
        configurarCartaoCredito();
    }
}

// Configura pagamento via Pix
function configurarPix() {
    const confirmarPagamento = document.getElementById('confirmar-pagamento');
    if (!confirmarPagamento) return;

    confirmarPagamento.addEventListener('click', function () {
        alert("Pagamento confirmado");
        window.location.href = "http://127.0.0.1:8000/produtos/listar";
    });

    gerarQRCodePix();
}

function gerarQRCodePix() {
    const payloadPix = gerarPayloadPixComCRC(`00020126330014BR.GOV.BCB.PIX0111224297487465204000053039865802BR5901N6001C62120508Benedito6304`);
    QRCode.toDataURL(payloadPix, function (error, url) {
        if (error) {
            console.error("Erro ao gerar QR Code:", error);
            return;
        }
        document.getElementById("qrcode").src = url;
        console.log("QR Code gerado com sucesso!");
    });
}

function calcularCRC16(payload) {
    const polinomio = 0x1021;
    let resultado = 0xffff;

    for (let i = 0; i < payload.length; i++) {
        resultado ^= payload.charCodeAt(i) << 8;
        for (let bit = 0; bit < 8; bit++) {
            resultado = (resultado & 0x8000) ? (resultado << 1) ^ polinomio : resultado << 1;
        }
        resultado &= 0xffff;
    }
    return resultado.toString(16).toUpperCase().padStart(4, "0");
}

function gerarPayloadPixComCRC(payloadBase) {
    const crc16 = calcularCRC16(payloadBase);
    return payloadBase + crc16;
}

function configurarCartaoCredito() {
    const pagarCartao = document.getElementById("validar-cartao");

    pagarCartao.addEventListener('click', function() {
        const cardNumber = document.getElementById('cardNumber');
        const expirationDate = document.getElementById('expirationDate');
        const cvv = document.getElementById('cvv');
        if (validarCartao(cardNumber, expirationDate, cvv)) {
            alert("Pagamento confirmado");
            window.location.href = "http://127.0.0.1:8000/produtos/listar";
        } else {
            alert("Dados do cartão inválidos!");
        }

    })
}

// Configura pagamento via cartão de crédito
// function configurarCartaoCredito() {
//     const pagarCartao = document.getElementById("validar-cartao");
//     if (!pagarCartao) return;

//     pagarCartao.addEventListener("click", function () {
//         const cardNumber = document.getElementById('cardNumber');
//         const expirationDate = document.getElementById('expirationDate');
//         const cvv = document.getElementById('cvv');
//         console.log(validarCartao(cardNumber, expirationDate, cvv))
//         if (validarCartao(cardNumber, expirationDate, cvv)) {
//             alert("Pagamento confirmado");
//             window.location.href = "http://127.0.0.1:8000/produtos/listar";
//         } else {
//             alert("Dados do cartão inválidos!");
//         }
//     });
// }

function validarCartao(cardNumber, expirationDate, cvv) {
     const cardRegex = /^\d{4} \d{4} \d{4} \d{4}$/; // Ex: 1234 5678 9012 3456
     const expirationRegex = /^(0[1-9]|1[0-2])\/\d{2}$/; // Ex: MM/AA
     const cvvRegex = /^\d{3}$/; // CVV de 3 dígitos

     return (
         cardRegex.test(cardNumber.value) &&
         expirationRegex.test(expirationDate.value) &&
         cvvRegex.test(cvv.value)
     );
}
