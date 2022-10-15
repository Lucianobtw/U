<?php

/* Enlaza el archivo config.php */
/* Contiene la información relacionada a la DB */

include_once 'config.php';

/* Se crea la la conexion mediante la función "new mysqli" */
$conn = new mysqli($servername, $username, $password, $dbname);

/* chequea si la conexion falló, si es así mostrará el error. */

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

/* se obtienen los valores mediante método post del formulario html */

$nombre = $_POST['Nombre'];
$apellido = $_POST['Apellido'];
$email = $_POST['email'];
$asunto = $_POST['Asunto'];

/* Procedimiento almacenado sql de insert */
$sql = "SELECT Primer_Nombre, Primer_Apellido, email, Asunto  FROM contacto";

/* Se ejecuta el procedimiento almacenado */
$result = $conn->query($sql);

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
