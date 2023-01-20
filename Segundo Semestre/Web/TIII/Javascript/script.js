
function AgregarInput() {

    const form = document.getElementById("forms");

    const input = document.createElement("input");
    input.setAttribute('name','valor');

    form.appendChild(input);

}

function Capturar() {

    let element = document.getElementsByName('valor');
    let suma = 0
    element.forEach((element) => {

        
        suma += parseInt(element.value);
    })
    console.log(suma);

    const insert = document.getElementById('div');
    let text = suma;
    insert.innerText =  text;

}

