<?php

/* Enlaza el archivo config.php */
/* Contiene la información relacionada a la DB */

include_once './config.php';

$id = $_POST['ID'];

/* Procedimiento almacenado sql de insert */
$sql = "DELETE FROM `contacto` WHERE ID = '$id'";

/* Se ejecuta el procedimiento almacenado */
$result = $conn->query($sql);

$response = array();

if ($result) {
    $response['success'] = "Solicitud eliminada correctamente";
    exit(json_encode($response));
} else {
    $response['error'] = "error" . $conn->error;
    exit(json_encode($response));
}

/* Se cierra la conexion */
$conn->close();
