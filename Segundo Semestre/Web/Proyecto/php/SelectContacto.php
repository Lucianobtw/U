<?php

/* Enlaza el archivo config.php */
/* Contiene la información relacionada a la DB */

include_once('./config.php');

/* Consulta SQL de SELECT */

$sql = "SELECT ID, Primer_Nombre, Primer_Apellido, email, Asunto FROM contacto";

/* Se ejecuta la consulta SQL */

$result = $conn->query($sql);

/* $response */
/* A partir de esta función se hace uso de $response el cual es un array asociativo similar a Json */
/* con este array se envian mensajes de estado dependiendo del resultado de cada función */

/* EN ESTE CASO al ser una consulta SELECT se almacenan las filas de la consulta en el array */
/* De esta forma pueden ser leidas e interpretadas como JSON en JS */

$response = array();

if ($result->num_rows > 0) {
    if ($result) {
        while ($row = $result->fetch_assoc()) {
            $response[] = $row;
        }
        exit(json_encode($response));
    } else {
        $response['error'] = "error" . $conn->error;
        exit(json_encode($response));
    }
}

/* Se cierra la conexion */
$conn->close();
