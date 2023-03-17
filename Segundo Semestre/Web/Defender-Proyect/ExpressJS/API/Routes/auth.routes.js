/* Se importa el rutificador de express */
import { Router } from "express";

/* Se importan los metodos de controlador correspondiente a cada tipo de peticion */
import { ValidateLogin, SignUpUser, LogOut } from "../controllers/index.controllers.js";

const router = Router();

router.post('/', ValidateLogin); // Peticion POST de login
router.post('/new', SignUpUser); // Peticion POST de registro
router.post('/exit', LogOut); // Peticion POST de logout

export default router;