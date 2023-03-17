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
        </div>

        <div class="nos-grids" id="l${obj.ID}">
            <img src="../assets/img/userlogo.jpg" alt="Defender-Logo" width="200px">
         </div>
        
        `;

        box.innerHTML += element;
    };
};

window.addEventListener("load", async (e) => {

    const nosbox = document.getElementById("nosotros-box");
    const data = await GetNosotros();
    CreateNosotros(data, nosbox);

});