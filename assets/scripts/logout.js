// logout.js
window.addEventListener('unload', function (e) {
    // Enviar uma solicitação ao servidor para fazer logout quando a janela do navegador for fechada
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/logout', false); // Faz uma solicitação GET para o endpoint de logout
    xhr.send();
});
