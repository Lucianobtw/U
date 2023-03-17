import { Pool } from "../../Database.js";

export const GETNosotros = async (req, res) => {

    try {
        const result = await Pool.query("SELECT * FROM Nosotros");
        const Nosotros = result[0];

        if (result) { res.status(200).json(Nosotros); }
    }

    catch (error) {
        res.status(500).json({ message: "Error al obtener solicitudes" });
    }
};

export const PUTNosotros = async (req, res) => {
    try {
        const { Nombre, email, Descripcion } = req.body;
        const PutID = req.params.id;

        const result = await Pool.query("UPDATE Nosotros SET Nombre = ?, email = ?, Descripcion = ? WHERE ID = ?",
            [Nombre, email, Descripcion, PutID]);

        if (result.affectedRows === 0) {
            return res.status(201).json({ message: 'No se encontro la id' });
        } else {
            res.status(200).json({ message: "Informacion actualizada" });
        };
    }

    catch (error) {
        res.status(500).json({ message: "Error al actualizar" });
    }
};