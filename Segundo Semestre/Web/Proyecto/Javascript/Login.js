"use strict";

/* Código correspondiente a los cambios de display */

let signspan = document.getElementById("sign-span");
let signbox = document.getElementById("signin-box");

let logspan = document.getElementById("log-span");
let logbox = document.getElementById("login-box");

signspan.addEventListener("click", (event) => {
    event.preventDefault();
    signbox.style.display = "grid";
    logbox.style.display = "none";
});

logspan.addEventListener("click", (event) => {
    event.preventDefault();
    logbox.style.display = "grid";
    signbox.style.display = "none";
});

/* Función que realiza petición a archivo login */
/* Recibe el mensaje de respuesta (obj.success) y en función del resultado se podrá acceder o no */

const ValidateLogin = async (data) => {
    const response = await fetch("./php/Login.php", {
        method: "POST",
        body: data,
    });

    const respuesta = await response.text();
    const obj = JSON.parse(respuesta);

    /* obj.success corresponde al mensaje de respuesta de Login.php */

    if (obj.success === "true") {
        location.href = "./Home.php";
    } else if (obj.success === "false") {
        alert(obj.message);
    }
};

let button = document.getElementById("btnLogin");
let form = document.getElementById("form-login");

button.addEventListener("click", async (e) => {
    e.preventDefault();
    let data = new FormData(form);
    await ValidateLogin(data);
});
