"use strict";

const ResponseDiv = (rdiv, text) => {

    rdiv.innerHTML = text;
    rdiv.style.display = "flex";

    setTimeout(() => { rdiv.style.display = "none" }, 3000);
};

/* Función que detecta si los campos están vacios */

const EmptyForm = (nombre, apellido, email, asunto, rdiv) => {
    if (nombre === "" || apellido === "" || email === "" || asunto === "") {
        ResponseDiv(rdiv, "Todos los campos son obligatorios");
        return false;
    } else {
        return true;
    }
};

/* Función que valida la longitud maxima aceptada segun la BD */

const ValidateDataLength = (nombre, apellido, email, asunto, rdiv) => {

    if (nombre.length > 25 || apellido.length > 25 || email.length > 50 || asunto.length > 500) {
        ResponseDiv(rdiv, "Uno o más campos superan el límite de caracteres");
        return false;
    } else {
        return true;
    }
};

/* Función que valida el email y su formato */

const ValidateNewMail = (email, rdiv) => {
    /* expresión regular de email */ /* luciano@gmail.com */
    let email_exp = /\w+@\w+\.+[a-z]/;

    if (!email_exp.test(email)) {
        ResponseDiv(rdiv, "El email no es válido");
        return false;
    } else {
        return true;
    } /* retorna true si el valor es un mail */
};

/* Funcion principal */

const InsertSolicitud = async (data, rdiv, form) => {

    const response = await fetch("http://localhost:3000/contact/new", {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            "Content-Type": "application/json",
        },
    });

    if (response.status == 200) { ResponseDiv(rdiv, "Solicitud enviada con éxito"); }

    form.reset();
};

const form = document.getElementById("formulario");

form.addEventListener("submit", async (e) => {

    e.preventDefault();

    const Nombre = document.getElementById("nombre").value;
    const Apellido = document.getElementById("apellido").value;
    const email = document.getElementById("email").value;
    const asunto = document.getElementById("asunto").value;
    const rdiv = document.getElementById("respuesta");

    const ValidateNewSol = () => {

        if (EmptyForm(Nombre, Apellido, email, asunto, rdiv) &&
            ValidateDataLength(Nombre, Apellido, email, asunto, rdiv) &&
            ValidateNewMail(email, rdiv)) {
            return true;
        } else {
            return false;
        }
    };


    if (ValidateNewSol() === true) {

        const data = {
            "Primer_Nombre": Nombre,
            "Primer_Apellido": Apellido,
            "email": email,
            "Asunto": asunto,
        };

        e.preventDefault();
        await InsertSolicitud(data, rdiv, form);
    }

});
