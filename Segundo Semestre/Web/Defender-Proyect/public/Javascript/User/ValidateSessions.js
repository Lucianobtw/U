"use strict";

const ValidateSession = (user, Admin, btn) => {

    if (user == null || Admin == null) {
        btn.style.display = "none";
        location.href = "./index.html";
    }
};

const ValidateAdmin = (Admin, btn) => {

    if (Admin == 0) {
        btn.style.display = "none";
    }
};

const user = sessionStorage.getItem("user");
const Admin = sessionStorage.getItem("Admin");
const Admbtn = document.getElementById("Admbtn");

window.addEventListener("load", () => {
    ValidateSession(user, Admin, Admbtn);
    ValidateAdmin(Admin, Admbtn);
});

