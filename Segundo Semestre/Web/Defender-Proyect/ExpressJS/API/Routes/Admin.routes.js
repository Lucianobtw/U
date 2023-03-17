
/* Se importa el rutificador de express */

import { Router } from "express";
import { GETNosotros, PUTNosotros } from "../controllers/Admin/Nosotros.controllers.js";
import { GetSolicitudes, DeleteSolicitud } from "../controllers/Admin/Contact.Admin.js";

const router = Router();

/* Peticiones para manipular informacion "Nosotros" */

router.get('/Nosotros/', GETNosotros); // Obtiene la informacion de la seccion "Nosotros"
router.put('/Nosotros/:id', PUTNosotros); // Actualiza la informacion de la seccion "Nosotros"

/* Peticiones para manipular solicitudes de contacto */

router.get('/', GetSolicitudes); // Obtiene todas las solicitudes de contacto
router.delete('/contacto/:id', DeleteSolicitud); // Elimina una solicitud de contacto

export default router;