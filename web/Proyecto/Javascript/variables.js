/* Strict mode makes it easier to write "secure" JavaScript. */
/* Strict mode changes previously accepted "bad syntax" into real errors. */

"use strict";

/* Función que recibe los datos de Select.php para mostrar mediante fetch el contenido de la DB */

async function enviarFormulario(datosFormulario) {
    const response = await fetch("./Insert.php", {
        method: "POST",
        body: datosFormulario,
    });

    const respuesta = await response.text();
    const obj = JSON.parse(respuesta);

    document.getElementById("respuesta").innerHTML = obj.success;
}

/* Función que recibe los datos de Select.php para mostrar mediante fetch el contenido de la DB */

async function recibedatos() {
    const response = await fetch("./Select.php", {
        method: "POST",
    });

    /* Estructura JSON:
        
        {   
            "person":  [  
                {
                    "Primer_Nombre":"Oscar",
                    "Primer_Apellido":"Mellado",
                    "email":"omellado@dwm.nz",
                    "Asunto":"hola"
                },
                {
                    "Primer_Nombre":"Luciano",
                    "Primer_Apellido":"Revillod",
                    "email":"lrevillod@dwm.nz",
                    "Asunto":"holi"
                }
            ]
        }    
    */

    const respuesta = await response.text();

    const obj = JSON.parse(respuesta);

    for (let i = 0; i < obj.length; i++) {
        let user = obj[i];

        const li = document.createElement("li");
        const h2 = document.createElement("h2");
        const h3 = document.createElement("h3");
        const p = document.createElement("p");

        h2.innerHTML = `${user.Primer_Nombre} ${user.Primer_Apellido}`;
        h3.innerHTML = `email: ${user.email}`;
        p.innerHTML = `Asunto: ${user.Asunto}`;

        li.appendChild(h2);
        li.appendChild(h3);
        li.appendChild(p);
        document.getElementById("lista").appendChild(li);
    }
}

/* Función que detecta si los campos están vacios */

function validar_campos(nombre, apellido, email, asunto) {
    /* uso de lógica mediante || ("o") */
    if (nombre === "" || apellido === "" || email === "" || asunto === "") {
        alert("Todos los campos son obligatorios");
        return false;
    } else {
        return true;
    } /* retorna true si todos los campos estan llenos */
}

/* Función que valida la longitud maxima aceptada segun la BD */

function validar_long(nombre, apellido, email, asunto) {
    /* lista con la longitud maxima de cada input según la DB */
    let num = [25, 25, 50, 500];
    let lista = [nombre, apellido, email, asunto];

    /* ciclo for que compara los valores indice a indice de ambas listas. */
    for (let i = 0; i < lista.length; i++) {
        if (lista[i].length > num[i]) {
            alert("El campo " + lista[i] + " es muy largo");
            return false;
        } else {
            return true;
        }
    } /* retorna true si la long de la cadena */
} /* de caracteres es menor a la correspondiente en el array 'num'  */

/* Función que valida si el email corresponde a la estructura de un email */

function validar_email(email) {
    /* expresión regular de email */ /* luciano@gmail.com */
    let email_exp = /\w+@\w+\.+[a-z]/;

    if (!email_exp.test(email)) {
        alert("El email no es válido");
        return false;
    } else {
        return true;
    } /* retorna true si el valor es un mail */
}

/* Función que valida si se cumplen todas las condiciones */

function validar() {
    /* variables de id's html, .value para obtener su valor a traves del formulario */
    let nombre, apellido, email, asunto;

    nombre = document.getElementById("nombre").value;
    apellido = document.getElementById("apellido").value;
    email = document.getElementById("email").value;
    asunto = document.getElementById("asunto").value;

    if (validar_campos(nombre, apellido, email, asunto) === true && validar_long(nombre, apellido, email, asunto) === true && validar_email(email) === true) {
        return true;
    } else {
        return false;
    } /* retorna true si todos los campos estan llenos y cumplen con las condiciones */
}

document.getElementById("formulario").addEventListener("submit", async function (event) {
    /* Se previene la carga por defecto de la pagina. */
    event.preventDefault();

    /* Si la función validar() retorna true, se ejecutan las funciones correspondientes  */

    if (validar()) {
        const formulario = document.getElementById("formulario");
        const formularioData = new FormData(formulario); /* class: con todos los input del form*/
        let ul = document.getElementById("lista");
        ul.innerHTML = "";
        await enviarFormulario(formularioData);
        formulario.reset();
        await recibedatos();
    }
});
