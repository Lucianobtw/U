"use strict";

const GetNosotros = async () => {

    const response = await fetch("http://localhost:3000/setup/Nosotros", {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    });

    const data = await response.json();
    return data;
};

const CreateNosotros = (data, box) => {

    box.innerHTML = "";

    for (let i = 0; i < data.length; i++) {

        const obj = data[i];

        const element = `   
        
        <div class="nos-grids" id="r${obj.ID}">
            <div class="nos-top">
                <h3>${obj.Nombre}</h3>
                <h4>${obj.email}</h4>
            </div>
            <div class="nos-body">${obj.Descripcion}</div>
            
            <form class="edit-form">
                <input type="text" id="Nombre${obj.ID}" value="${obj.Nombre}">
                <input type="text" id="email${obj.ID}" value="${obj.email}">
                <input class="bttm" id="Descripcion${obj.ID}" value="${obj.Descripcion}"></input>
            </form>
        
        </div>

        <div class="nos-grids" id="l${obj.ID}">
            <img src="../assets/img/userlogo.jpg" alt="Defender-Logo" width="200px">
            <button onclick="EditNosotros(${obj.ID})">Editar Informacion</button>
         </div>
        
        `;

        box.innerHTML += element;
    };
};

const NosotrosBTN = document.getElementById("nav-li-3");

NosotrosBTN.addEventListener("click", async () => {

    nosbox.innerHTML = "";
    userbox.style.display = "none";
    solbox.style.display = "none";
    nosbox.style.display = "grid";

    const FuncNos = await GetNosotros();
    CreateNosotros(FuncNos, nosbox);
});

const EditNosotros = async (id) => {

    const Nombre = document.getElementById("Nombre" + id).value;
    const email = document.getElementById("email" + id).value;
    const Descripcion = document.getElementById("Descripcion" + id).value;

    const response = await fetch("http://localhost:3000/setup/Nosotros/" + id, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            "Nombre": Nombre,
            "email": email,
            "Descripcion": Descripcion
        }),
    });

    if (response.status == 200) {
        const FuncGET = await GetNosotros();
        CreateNosotros(FuncGET, nosbox);
    } else if (response.status == 201) {
        alert("Error al editar");
    };
};

