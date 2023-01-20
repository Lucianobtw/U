/* Función que recibe los elementos mediante JSON de php SELECT */

const ShowContact = async (contact) => {
    const response = await fetch("./php/SelectContacto.php", {
        method: "POST",
    });

    const respuesta = await response.text();
    const obj = JSON.parse(respuesta);

    let l = obj.length;

    /* Por cada uno de los elementos existentes */
    /* Se crean elementos HTML */

    for (let i = 0; i < l; i++) {
        let solicitud = obj[i];

        let li = document.createElement("li");
        li.setAttribute("class", "contactcard");
        li.setAttribute("onclick", "EditContact(" + solicitud.ID + ")");

        /* Asigno funcion onclick la cual me entregará la ID de la solicitud de contacto */
        /* que necesito para realizar un UPDATE */

        let div = document.createElement("div");
        div.setAttribute("class", "contactop");

        let h2 = document.createElement("h2");
        h2.innerHTML = `${solicitud.Primer_Nombre + " " + solicitud.Primer_Apellido}`;

        let p = document.createElement("p");
        p.innerHTML = `${solicitud.Asunto}`;

        div.appendChild(h2);

        li.appendChild(div);
        li.appendChild(p);

        contact.appendChild(li);
    }
};

/* Función que se ejecuta ONCLICK recibe la id de una solicitud de contacto */
/* Existe un formulario invisible que almacenara la información de la solicitud en cuestión */

const EditContact = async (id) => {
    const response = await fetch("./php/SelectContacto.php", {
        method: "POST",
    });

    const respuesta = await response.text();
    const obj = JSON.parse(respuesta);

    let l = obj.length;

    for (let i = 0; i < l; i++) {
        let solicitud = obj[i];

        /* Se itera a través de las solicitudes, si el parametro coincide con alguno de la iteración */
        /* Se completa con .value el formulario con los valores que corresponde */

        if (solicitud.ID == id) {
            document.getElementById("ID").value = solicitud.ID;
            document.getElementById("EditNombre").value = solicitud.Primer_Nombre;
            document.getElementById("EditApellido").value = solicitud.Primer_Apellido;
            document.getElementById("EditEmail").value = solicitud.email;
            document.getElementById("EditMensaje").value = solicitud.Asunto;
        }
    }
};

/* Función que realiza petición de DELETE a archivo php */

const DeleteContact = async (data) => {
    const response = await fetch("./php/DeleteContacto.php", {
        method: "POST",
        body: data,
    });

    /* Recibo la respuesta y muestro el estado de la petición */

    const respuesta = await response.text();
    const obj = JSON.parse(respuesta);

    alert(obj.success);
};

/* Función que realiza petición de UPDATE a archivo php */

const UpdateContact = async (data) => {
    const response = await fetch("./php/UpdateContacto.php", {
        method: "POST",
        body: data,
    });

    /* Recibo la respuesta y muestro el estado de la petición */

    const respuesta = await response.text();
    const obj = JSON.parse(respuesta);

    alert(obj.success);
};

let contact = document.getElementById("left");

let Dbtn = document.getElementById("e-delete");
let Ubtn = document.getElementById("e-update");

let form = document.getElementById("fright");

/* Al cargar la página se ejecuta la función ShowContact para mostrar las solicitudes*/

window.addEventListener("load", async function (e) {
    contact.innerHTML = "";
    e.preventDefault();
    await ShowContact(contact);
});

/* Ejecuto DELETE y actualizo la información mediante ShowContact() */

Dbtn.addEventListener("click", async function (e) {
    e.preventDefault();
    let data = new FormData(form);
    await DeleteContact(data);
    contact.innerHTML = "";
    await ShowContact(contact);
    form.reset();
});

/* Ejecuto UPDATE y actualizo la información mediante ShowContact() */

Ubtn.addEventListener("click", async function (e) {
    e.preventDefault();
    let data = new FormData(form);
    await UpdateContact(data);
    contact.innerHTML = "";
    await ShowContact(contact);
    form.reset();
});
