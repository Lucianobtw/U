"use strict";

/* Código correspondiente a los cambios de display */

let signspan = document.getElementById("signup-span");
let signbox = document.getElementById("signup-box");

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