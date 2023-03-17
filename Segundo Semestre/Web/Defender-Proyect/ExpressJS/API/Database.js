/* Importo metodo que permite conexion a bd mysql */

import { createPool } from 'mysql2/promise';
import MysqlStore from "express-mysql-session";

/* Credenciales .env */

import { HOST, USER, PASSWORD, DB_PORT, DATABASE } from './config.js';

/* se crea y exporta la conexion */

export const Pool = createPool({
    host: HOST,
    user: USER,
    password: PASSWORD,
    port: DB_PORT,
    database: DATABASE
});

/* Uso de sesiones con MySQL */

export const sessionStore = new MysqlStore({
    expiration: (1825 * 86400 * 1000),
    endConnectionOnClose: false
}, Pool);

