import { Pool } from "../Database.js";

export const InsertSolicitud = async (req, res) => {

    try {
        const { Primer_Nombre, Primer_Apellido, email, Asunto } = req.body;

        const result = await Pool.query("INSERT INTO contacto (Primer_Nombre, Primer_Apellido, email, Asunto) VALUES (?, ?, ?, ?)",
            [Primer_Nombre, Primer_Apellido, email, Asunto]
        );

        if (result) { res.status(200).json({ message: "Usuario registrado" }); }
    }

    catch (error) {
        res.status(500).json({ message: "Error al registrar usuario" });
    }
};