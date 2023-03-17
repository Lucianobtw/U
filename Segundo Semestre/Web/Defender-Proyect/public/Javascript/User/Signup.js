"use strict";

/* Función que detecta si los campos están vacios */

const ResponseDiv = (rdiv, text) => {

    rdiv.innerHTML = text;
    rdiv.style.display = "flex";

    setTimeout(() => { rdiv.style.display = "none" }, 3000);

};

const EmptyUser = (Rut, Username, email, pass, repass, rdiv) => {
    if (Rut === "" || Username === "" || email === "" || pass === "" || repass === "") {
        ResponseDiv(rdiv, "Todos los campos son obligatorios");
        return false;
    } else {
        return true;
    }
};

/* Funcion que valida si las contraseñas ingresadas coinciden */

const ValidatePass = (pass, repass, rdiv) => {
    if (pass === repass) {
        return true;
    } else {
        ResponseDiv(rdiv, "Las contraseñas no coinciden");
        return false;
    }
};

/* Función que valida la longitud del rut ingresado */

const ValidateRut = (Rut, rdiv) => {
    if (Rut.length === 8) {
        return true;
    } else {
        ResponseDiv(rdiv, "El rut debe tener 8 caracteres");
        return false;
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

const ValidateDataLength = (Rut, Username, email, pass, repass, rdiv) => {

    if (Rut.length > 8 || Username.length > 25 || email.length > 50 || pass.length > 25 || repass.length > 25) {
        ResponseDiv(rdiv, "Uno o más campos superan el límite de caracteres");
        return false;
    } else {
        return true;
    }
}

const InsertNewUser = async (data, rdiv, form) => {
    const response = await fetch("http://localhost:3000/signup/new", {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            "Content-Type": "application/json",
        },
    });

    if (response.status == 200) { // 200 = OK

        rdiv.innerHTML = "Te haz registrado exitosamente";
        rdiv.style.display = "flex";

        setTimeout(() => {
            rdiv.style.display = "none"
            form.reset();
            location.reload();
        }, 2000);

    } else if (response.status == 201) { // 201 = Usuario ya existe
        ResponseDiv(rdiv, "El usuario ya existe");
        form.reset();
    };
}

const signbtn = document.getElementById("btn-signup");

signbtn.addEventListener("click", async (e) => {

    const NewRut = document.getElementById("newrut").value;
    const NewUser = document.getElementById("s-user").value;
    const NewEmail = document.getElementById("s-email").value;
    const NewPass = document.getElementById("s-pass").value;
    const repass = document.getElementById("s-pass2").value;
    const rdiv = document.getElementById("response");


    const ValidateNewSign = () => {

        if (EmptyUser(NewRut, NewUser, NewEmail, NewPass, repass, rdiv) &&
            ValidateRut(NewRut, rdiv) && ValidateNewMail(NewEmail, rdiv) &&
            ValidatePass(NewPass, repass, rdiv) &&
            ValidateDataLength(NewRut, NewUser, NewEmail, NewPass, repass, rdiv)) {
            return true;
        } else {
            return false;
        }
    };

    if (ValidateNewSign() === true) {

        const form = document.getElementById("form-sign");

        const data = {
            "Rut": NewRut,
            "Username": NewUser,
            "email": NewEmail,
            "password": NewPass,
        };

        e.preventDefault();
        await InsertNewUser(data, rdiv, form);
    }

});
