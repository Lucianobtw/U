"use strict";

/* Código correspondiente a los cambios de display */

let signspan = document.getElementById("signup-span");
let signbox = document.getElementById("signup-box");

let logspan = document.getElementById("log-span");
let logbox = document.getElementById("login-box");

signspan.addEventListener("click", (event) => {
    event.preventDefault();
    setTimeout(() => {
        signbox.style.display = "grid";
        logbox.style.display = "none";
    }, 200);
});

logspan.addEventListener("click", (event) => {
    event.preventDefault();
    setTimeout(() => {
        logbox.style.display = "grid";
        signbox.style.display = "none";
    }, 200);
});