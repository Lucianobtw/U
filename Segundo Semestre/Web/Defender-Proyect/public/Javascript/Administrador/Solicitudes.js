"use strict";

const GETsolicitudes = async () => {

    const response = await fetch("http://localhost:3000/setup/", {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    });

    const data = await response.json();
    return data;
};

const ShowModal = (id) => {

    const dialog = document.getElementById(id);
    dialog.showModal();

    dialog.style.display = "flex";

    dialog.addEventListener("click", (e) => {
        if (e.target === dialog) {
            dialog.close();
            dialog.style.display = "none";
        }
    });

    window.addEventListener("keydown", (e) => {
        if (e.key === "Escape") {
            dialog.close();
            dialog.style.display = "none";
        }
    });
};


const CreateElements = (data, box) => {

    box.innerHTML = "";

    for (let i = 0; i < data.length; i++) {

        const Solicitud = data[i];

        const element = `   
        
        <div class="users-li">
            <div class="user-info">
                <h3 class="h3-name">${Solicitud.Primer_Nombre + " " + Solicitud.Primer_Apellido}</h3>
                <h4 class="h4-mail">${Solicitud.email}</h4>
            </div>

            <div class="user-btns">
                <button class="user-del-btn" onclick="DeleteSolicitud(${Solicitud.ID})">Eliminar solicitud</button>
                <button class="user-edit-btn" onclick="ShowModal(${Solicitud.ID})">Ver asunto</button>
            </div>
        </div>
        
        <dialog id="${Solicitud.ID}" class="modal">
            <div class="dialog-box">

                <div class="modal-top"> 
                    <img src="../assets/img/Logo.png" alt="Logo" class="logo" width="50px">
                    <h2 class="h2-modal">Defender</h2>
                </div>

                <div class="dialog-header">
                    <h3 class="h3-name">${Solicitud.Primer_Nombre + " " + Solicitud.Primer_Apellido}</h3>
                    <h4 class="h4-mail">${Solicitud.email}</h4>
                </div>
                <div class="dialog-body">
                    <h4 class="h4-asunto">Asunto:</h4>
                    <p class="p-asunto">${Solicitud.Asunto}</p>
                </div>    
            </div>
        </dialog>
        
        `;

        box.innerHTML += element;
    };
};

const GetSolicitudesBtn = document.getElementById("nav-li-2");
const userbox = document.getElementById("users-box");
const solbox = document.getElementById("solicitudes-box");
const nosbox = document.getElementById("nosotros-box");

GetSolicitudesBtn.addEventListener("click", async (e) => {

    solbox.innerHTML = "";
    nosbox.style.display = "none";
    userbox.style.display = "none";
    solbox.style.display = "grid";

    const FuncData = await GETsolicitudes();
    e.preventDefault();
    CreateElements(FuncData, solbox);

});

const DeleteSolicitud = async (id) => {

    const response = await fetch("http://localhost:3000/setup/contacto/" + id, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
        },
    });

    const FuncSolicitudes = await GETsolicitudes();

    if (response.status == 200) { CreateElements(FuncSolicitudes, solbox); }
};