// https://github.com/github/fetch

const send = document.getElementById('send')

send.addEventListener('click', (e) =>{
    fetch("https://formsubmit.co/ajax/wilhemmaxime97@gmail.com", {
    method: "POST",
    headers: { 
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    },
    body: JSON.stringify({
        name: "Wilhem Wundt",
        message: 'Meu amor hoje é um dia especial para nos se divertir durante nosso tempo em mexico!'
    })
})
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.log(error));
})

// -----------------------------------------------------------------------------------------------

var numeros = [1, 2, 3, 4, 5];
var quadrados = numeros.map(function(numero) {
    console.log(numero * numero);
});
var pares = numeros.filter(function(numero) {
    return numero % 2 === 0;
});
var soma = numeros.reduce(function(acumulador, numero) {
    return acumulador + numero;
}, 0);



function valoresM(){
    numeros.forEach(numero => {
        var mul =  numero * numero
        return mul
    });
}
console.log(valoresM());

