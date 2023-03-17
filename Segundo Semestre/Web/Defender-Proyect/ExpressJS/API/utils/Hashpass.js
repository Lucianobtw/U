/* Se importa el modulo sha512 para encriptar cadenas de texto */
import { sha512 } from "js-sha512";

/* Se exporta la funcion, lo cual permitira usarla como modulo */
export const Hashpass = async (password) => {
    const hash = sha512(password);
    return hash;
};