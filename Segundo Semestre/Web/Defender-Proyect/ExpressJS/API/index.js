import express from "express";
import session from "express-session";
import { sessionStore } from "./Database.js";

/* Rutas (router) */

import indexRoutes from "./Routes/auth.routes.js";
import AdminRoutes from "./Routes/Admin.routes.js";
import ContactRoutes from "./Routes/user.routes.js";

/* .env (configuracion y credenciales) */

import './config.js';
import { PORT } from "./config.js";

import cors from "cors";
import bodyParser from "body-parser";

const app = express();

/* Se utiliza la transferencia de datos en JSON */

app.use(express.json());

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.use(cors());

/* Se hace uso de sesiones */

app.use(session({
    key: "DefenderKey",
    secret: "DefenderSecret",
    store: sessionStore,
    resave: false,
    saveUninitialized: false,
}));

/* Rutas base asignadas*/

app.use('/setup', AdminRoutes)
app.use('/login', indexRoutes);
app.use('/signup', indexRoutes);
app.use('/logout', indexRoutes);

app.use('/contact', ContactRoutes);

app.use((req, res, next) => {
    res.status(404).json({ message: "Not found" })
});

/* Puerto asignado al servidor (.env) */

app.listen(PORT)

// console.log('Server on port ' + PORT);