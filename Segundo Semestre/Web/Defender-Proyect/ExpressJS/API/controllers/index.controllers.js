/* Se importan los modulos de conexion a bd y encriptacion */

import { Pool } from "../Database.js";
import { Hashpass } from '../utils/Hashpass.js'

export const ValidateLogin = async (req, res) => {

    try {
        const { logUsername, logpassword } = req.body;
        const hash = await Hashpass(logpassword);

        const result = await Pool.query("SELECT * FROM Usuarios WHERE Username = ? AND password = ?", [logUsername, hash]);
        const consulta = result[0];
        const user = consulta[0];

        if (consulta.length > 0) {
            req.session.user = user.Username;
            req.session.Admin = user.Admin;

            res.status(200).json({
                user: req.session.user,
                Admin: req.session.Admin,
            });
            console.log("[STATUS] - Se ha logueado el usuario: " + req.session.user + "");
        } else {
            res.status(201).json({ msg: "Usuario no encontrado" });
        }
    }

    catch (error) {
        res.status(404).json({ message: "Error al logear usuario" });
    }
};

export const SignUpUser = async (req, res) => {

    try {
        const { Rut, Username, email, password } = req.body;
        const hash = await Hashpass(password);

        const comprobe = await Pool.query("SELECT * FROM Usuarios WHERE RUT = ? OR Username = ? OR email = ?", [Rut, Username, email]);
        const consulta = comprobe[0];

        if (consulta.length > 0) {
            res.status(201).json({ msg: "Usuario ya existe" });

        } else {

            const result = await Pool.query(
                "INSERT INTO Usuarios (RUT, Username, email, password, Admin) VALUES (?, ?, ?, ?, ?)",
                [Rut, Username, email, hash, 0]
            );

            if (result) {
                res.status(200).json({ msg: "Usuario registrado" });
            }
        }
    }

    catch (error) {
        res.status(404).json({ message: "Error al registrar usuario" });
    }
};

export const LogOut = async (req, res) => {

    try {
        req.session.destroy();
        res.status(200).json({ msg: "Usuario deslogeado" });
    }

    catch (error) {
        res.status(404).json({ message: "Error al deslogear usuario" });
    }
};