
/* Se importa el rutificador de express */
import { Router } from "express";
import { InsertSolicitud } from "../controllers/Contact.controllers.js";

const router = Router();

router.post('/new', InsertSolicitud); // Peticion POST de INSERT Solicitudes de Contacto

export default router;