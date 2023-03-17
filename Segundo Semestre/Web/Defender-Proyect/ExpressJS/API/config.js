/* Se importa el modulo que oermite leer variables de entorno */

import { config } from 'dotenv';

config();

/* Se exportan las variables y se les asignan valores por defecto  */

export const PORT = process.env.PORT || 3000;
export const HOST = process.env.DB_HOST || 'localhost';
export const USER = process.env.DB_USER || 'root';
export const PASSWORD = process.env.DB_PASS || '28081911';
export const DATABASE = process.env.DB_NAME || 'DefenderDB';
export const DB_PORT = process.env.DB_PORT || 3306;
export const SECRET = process.env.SECRET || 'DefaultSecret';