<?php

/* Enlaza el archivo config.php */
/* Contiene la información relacionada a la DB */

include_once('./config.php');

/* Se obtienen las variables POST desde HTML */

$id = $_POST['ID'];
$Pnombre = $_POST['EditNombre'];
$Papellido = $_POST['EditApellido'];
$Email = $_POST['EditEmail'];
$Emensaje = $_POST['EditMensaje'];

/* Consulta SQL de Update */

$sql = "UPDATE `contacto` SET `Primer_Nombre`='$Pnombre',`Primer_Apellido`='$Papellido',`email`='$Email',`Asunto`='$Emensaje' WHERE `ID` = '$id'";

/* Se ejecuta la consulta SQL */

$result = $conn->query($sql);

/* $response */
/* A partir de esta función se hace uso de $response el cual es un array asociativo similar a Json */
/* con este array se envian mensajes de estado dependiendo del resultado de cada función */
/* estos estados seran detectador por JS y serán mostrados en forma de alertas o texto plano en la WEB. */

$response = array();

if ($result) {
    $response['success'] = "Solicitud editada correctamente";
    exit(json_encode($response));
} else {
    $response['error'] = "error" . $conn->error;
    exit(json_encode($response));
}

/* Se cierra la conexion */

$conn->close();
