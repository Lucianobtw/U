"use strict";

const ValidateLogin = async (data, div) => {

    const response = await fetch("http://localhost:3000/login/", {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            "Content-Type": "application/json",
        },
    });

    const res = await response.json();
    const user = res.user;
    const Admin = res.Admin;

    if (response.status == 200) {

        sessionStorage.setItem("user", user);
        sessionStorage.setItem("Admin", Admin);

        location.href = "./Home.html";

    } else if (response.status == 201) {

        div.innerHTML = "Usuario o contraseña incorrectos";
        div.style.display = "flex";

        setTimeout(() => {

            div.innerHTML = "";
            div.style.display = "none";

        }, 2000);
    }
};

let loginbtn = document.getElementById("btn-login");

loginbtn.addEventListener("click", async (e) => {

    let logUser = document.getElementById("logUser").value;
    let logPass = document.getElementById("logPass").value;

    const data = {
        "logUsername": logUser,
        "logpassword": logPass,
    };

    let rdiv = document.getElementById("responselog");

    e.preventDefault();
    await ValidateLogin(data, rdiv);

});