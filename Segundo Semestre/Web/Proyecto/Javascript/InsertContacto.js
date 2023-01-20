/* Strict mode makes it easier to write "secure" JavaScript. */
/* Strict mode changes previously accepted "bad syntax" into real errors. */

"use strict";

/* Función que recibe un mensaje de confirmación mediante Insert.php */

let rdiv = document.getElementById("respuesta");

const InsertContacto = async (data, rdiv) => {
    const response = await fetch("./php/InsertContacto.php", {
        method: "POST",
        body: data,
    });

    const respuesta = await response.text();
    const obj = JSON.parse(respuesta);

    rdiv.innerHTML = "";
    rdiv.style.display = "flex";
    rdiv.innerHTML = obj.success;
};

/* Función que detecta si los campos están vacios */

const EmptyForm = (nombre, apellido, email, asunto, rdiv) => {
    if (nombre === "" || apellido === "" || email === "" || asunto === "") {
        rdiv.innerHTML = "";
        rdiv.style.display = "flex";
        rdiv.innerHTML = "Todos los campos son obligatorios";
        return false;
    } else {
        return true;
    }
};

/* Función que valida la longitud maxima aceptada segun la BD */

const DataLength = (nombre, apellido, email, asunto, rdiv) => {
    let num = [25, 25, 50, 500];
    let lista = [nombre, apellido, email, asunto];
    let nombres = ["nombre", "apellido", "email", "asunto"];

    for (let i = 0; i < lista.length; i++) {
        if (lista[i].length > num[i]) {
            rdiv.innerHTML = "";
            rdiv.style.display = "flex";
            rdiv.innerHTML = "El campo " + nombres[i] + " es muy largo";
            return false;
        } else {
            return true;
        }
    }
};

/* Función que valida si el email es valido  */

const ValidateEmail = (email, rdiv) => {
    let email_exp = /\w+@\w+\.+[a-z]/;

    if (!email_exp.test(email)) {
        rdiv.innerHTML = "";
        rdiv.style.display = "flex";
        rdiv.innerHTML = "El email no es valido";
        return false;
    } else {
        return true;
    }
};

/* Función que valida si se cumplen todas las condiciones */

const ValidateAll = () => {
    const nombre = document.getElementById("nombre").value;
    const apellido = document.getElementById("apellido").value;
    const email = document.getElementById("email").value;
    const asunto = document.getElementById("asunto").value;

    if (EmptyForm(nombre, apellido, email, asunto, rdiv) === true && DataLength(nombre, apellido, email, asunto, rdiv) === true && ValidateEmail(email, rdiv) === true) {
        return true;
    } else {
        return false;
    }
};

let form = document.getElementById("formulario");

/* Se escuchan los eventos provenientes de "form" */

/* Si se cumple la validación general se ejecuta la función que Inserta contenido */
/* Además se resetea el formulario y se muestra el contenido en un div*/
/* Utilizo función Timer para ocultar el mensaje luego de 5 segundos */

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    if (ValidateAll() === true) {
        let data = new FormData(form);
        await InsertContacto(data, rdiv);
        form.reset();
    }
    setTimeout(() => {
        rdiv.style.display = "none";
    }, 5000);
});
