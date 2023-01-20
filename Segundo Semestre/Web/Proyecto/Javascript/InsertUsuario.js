"use strict";

/* Función que detecta si los campos están vacios */

const EmptyUser = (Rut, Username, email, pass, repass) => {
    if (Rut === "" || Username === "" || email === "" || pass === "" || repass === "") {
        alert("Todos los campos son obligatorios");
        return false;
    } else {
        return true;
    }
};

/* Funcion que valida si las contraseñas ingresadas coinciden */

const ValidatePass = (pass, repass) => {
    if (pass == repass) {
        return true;
    } else {
        alert("Las contraseñas no coinciden");
        return false;
    }
};

/* Función que valida la longitud del rut ingresado */

const ValidateRut = (Rut) => {
    if (Rut.length === 8) {
        return true;
    } else {
        alert("El rut no es válido");
        return false;
    }
};

/* Función que valida el email y su formato */

const ValidateNewMail = (email) => {
    /* expresión regular de email */ /* luciano@gmail.com */
    let email_exp = /\w+@\w+\.+[a-z]/;

    if (!email_exp.test(email)) {
        alert("El email no es válido");
        return false;
    } else {
        return true;
    } /* retorna true si el valor es un mail */
};

/* Función que valida la longitud maxima aceptada segun la BD */

const ValidateSignLength = (a, b, c, x) => {
    /* lista con la longitud maxima de cada input según la DB */
    let num = [25, 25, 50, 500];
    let lista = [a, b, c, x];

    for (let i = 0; i < lista.length; i++) {
        if (lista[i].length > num[i]) {
            alert("El campo " + lista[i] + " es muy largo");
            return false;
        } else {
            return true;
        }
    } /* ciclo for que compara los valores indice a indice de ambas listas. */
    /* retorna true si la long de la cadena */
};

const ValidateNewSign = () => {
    let Rut = document.getElementById("newrut").value;
    let Username = document.getElementById("s-user").value;
    let email = document.getElementById("s-email").value;
    let pass = document.getElementById("s-pass").value;
    let repasss = document.getElementById("s-pass2").value;

    if (EmptyUser(Rut, Username, email, pass, repasss) && ValidateRut(Rut) && ValidateNewMail(email) && ValidatePass(pass, repasss) && ValidateSignLength(Rut, Username, email, pass)) {
        return true;
    } else {
        return false;
    }
};

const InsertNewUser = async (data) => {
    const response = await fetch("./php/InsertUsuario.php", {
        method: "POST",
        body: data,
    });

    const respuesta = await response.text();
    const obj = JSON.parse(respuesta);

    alert(obj.status);
};

let signbtn = document.getElementById("btnSignin");

signbtn.addEventListener("click", async function (event) {
    let formulario = document.getElementById("form-sign");
    event.preventDefault();

    if (ValidateNewSign()) {
        let data = new FormData(formulario);

        await InsertNewUser(data);
        formulario.reset();
        location.reload();
    }
});
