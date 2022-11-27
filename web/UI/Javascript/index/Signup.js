const InsertNewUser = async (data) => {
    const response = await fetch("https://expressjs-api-production.up.railway.app/signup", {
        method: "POST",
        body: data,
    });

    const respuesta = await response.text();
    const obj = JSON.parse(respuesta);
};

let signbtn = document.getElementById("btn-signup");

let NewRut = document.getElementById("newrut");
let NewUser = document.getElementById("newuser");
let NewEmail = document.getElementById("newemail");
let NewPass = document.getElementById("s-pass");

signbtn.addEventListener("click", async (e) => {

    const data = {
        Rut : NewRut.value,
        Username : NewUser.value,
        email : NewEmail.value,
        password : NewPass.value,
        Admin : 0,
    }

    e.preventDefault();
    await InsertNewUser(data);
});