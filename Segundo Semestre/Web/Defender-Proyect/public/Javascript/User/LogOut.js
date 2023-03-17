"use strict";

const LogOut = async () => {

    const response = await fetch("http://localhost:3000/logout/exit", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
    });

    if (response.status == 200) {
        sessionStorage.clear();
        localStorage.clear();
        location.href = "./index.html";
    }
};

const button = document.getElementById("logout-btn");

button.addEventListener("click", async (e) => {
    await LogOut();
});