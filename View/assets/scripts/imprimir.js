function imprimirConteudo() {
    var conteudo = document.querySelector('.Quadrado').innerHTML;
    var janelaImprimir = window.open('', 'Impressão', 'height=600, width=800');
    janelaImprimir.document.write('<html><head><title>Impressão</title>');
        janelaImprimir.document.write('<style>body { text-align: center;padding-top:450px; font-size: 60px; font-style: bold; font-family: sans-serif; }</style>');
        janelaImprimir.document.write('</head><body>');
        janelaImprimir.document.write(conteudo);
        janelaImprimir.document.write('</body></html>');
        // Imprime o conteúdo na nova janela
        janelaImprimir.print();
        // Fecha a nova janela após a impressão
        janelaImprimir.close();
}