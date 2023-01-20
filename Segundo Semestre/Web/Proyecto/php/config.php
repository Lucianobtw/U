<?php

/* Es importante guardar la información de conexión en un archivo adicional */
/* Si se trabaja en un repositorio se puede ignorar el archivo mediante .gitignore */

$servername = "db.inf.uct.cl";
$dbusername = "A2022_lrevillod";
$dbpassword = "A2022_lrevillod";
$dbname = "A2022_lrevillod";

/* $conn = variable que almacena la conexion a la bd */

$conn = new mysqli($servername, $dbusername, $dbpassword, $dbname);

/* Si se produce algún error de conexión se mostrará con el mensaje indicado */

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
