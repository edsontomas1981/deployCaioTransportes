// Define os dados do gráfico
var data = {
    labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    datasets: [{
        label: 'Guarulhos',
        data: [12, 19, 3, 5, 2, 0, 0, 0, 0, 0, 0, 0],
        // backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'red',
        borderWidth: 3,
        fill: false, // Desativa o preenchimento da área
    },
    {
        label: 'São Paulo',
        data: [0, 0, 0, 0, 0, 5, 8, 12, 15, 10, 8, 4], // Dados fictícios, substitua pelos seus dados
        // backgroundColor: 'rgba(255, 99, 132, 0.2)', // Cor de fundo
        borderColor: 'blue', // Cor da borda
        borderWidth: 3,
        fill: false // Desativa o preenchimento da área
    },
    {
    label: 'Santos',
    data: [0, 0, 0, 0, 0, 10, 16, 24, 30, 20, 4, 2], // Dados fictícios, substitua pelos seus dados
    // backgroundColor: 'rgba(255, 99, 132, 0.2)', // Cor de fundo
    borderColor: 'green', // Cor da borda
    borderWidth: 3,
    fill: false // Desativa o preenchimento da área
    }],
    
};

document.addEventListener('DOMContentLoaded', function() {
   // Obtém o contexto do canvas
   var ctx = document.getElementById('entregasNoPrazoPorFilial').getContext('2d');
    // Configurações do gráfico
    var options = {
        scales: {
            y: {
                beginAtZero: true
            }
        },
        title: {
            display: true,
            text: '',
            fontSize:16,
            fontColor: 'black',
        },
        legend: {
            position: 'right' // Define a posição da legenda para 'direita'
        },
    };

    // Cria o gráfico
    var myChart = new Chart(ctx, {
        type: 'line',
        data: data,
        options: options
    });



})
