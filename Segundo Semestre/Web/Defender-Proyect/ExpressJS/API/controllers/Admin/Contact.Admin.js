import { Pool } from "../../Database.js";

export const GetSolicitudes = async (req, res) => {

    try {
        const result = await Pool.query("SELECT * FROM contacto");
        const Solicitudes = result[0];

        if (result) { res.status(200).json(Solicitudes); }
    }

    catch (error) {
        res.status(500).json({ message: "Error al obtener solicitudes" });
    }
};


export const DeleteSolicitud = async (req, res) => {

    try {
        const { id } = req.params;

        const result = await Pool.query("DELETE FROM contacto WHERE ID = ?", [id]);

        if (result) { res.status(200).json({ message: "Solicitud eliminada" }); }

    } catch (error) {
        res.status(500).json({ message: "Error al eliminar solicitud" });
    }
};