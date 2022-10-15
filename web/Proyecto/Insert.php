<?php

/* Enlaza el archivo config.php */
/* Contiene la información relacionada a la DB */

include_once './config.php';

/* se obtienen los valores mediante método post del formulario html */

$nombre = $_POST['Nombre'];
$apellido = $_POST['Apellido'];
$email = $_POST['email'];
$asunto = $_POST['Asunto'];


/* Función que detecta si los campos están vacios */

function validarcampos($nombre, $apellido, $email, $asunto)
{
    if (empty($nombre) || empty($apellido) || empty($email) || empty($asunto)) {
        return false;
    } else {
        return true;
    } /* retorna true si todos los campos estan llenos */
}

/* Función que valida la longitud maxima aceptada segun la BD */

function validarlong($nombre, $apellido, $email, $asunto)
{
    /* lista con la longitud maxima de cada input según la DB */
    $num = array(25, 25, 50, 500);
    $lista = array($nombre, $apellido, $email, $asunto);

    /* ciclo for que compara los valores indice a indice de ambas listas. */
    for ($i = 0; $i < count($lista); $i++) {
        if (strlen($lista[$i]) > $num[$i]) {
            return false;
        } else {
            return true;
        }
    } /* retorna true si la long de la cadena */
}   /* de caracteres es menor a la correspondiente en el array 'num'  */


/* Función que valida si el email corresponde a la estructura de un email */

function validarmail($email)
{
    /* Se verifica si $email es una direccion de email */
    if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
        return true;
    } else {
        return false;
    }
} /* retorna true si el valor es un mail */

/* Valida si se cumplen todas las condiciones */

function validar($nombre, $apellido, $email, $asunto)
{
    if (
        validarcampos($nombre, $apellido, $email, $asunto) == true &&
        validarlong($nombre, $apellido, $email, $asunto) == true &&
        validarmail($email) == true
    ) {
        return true;
    } else {
        return false;
    }
} /* retorna true si todos los campos estan llenos y cumplen con las condiciones */


if (validar($nombre, $apellido, $email, $asunto) == true) {
    /* Se crea la la conexion mediante la función "new mysqli" */

    $conn = new mysqli($servername, $username, $password, $dbname);

    /* chequea si la conexion falló, si es así mostrará el error. */

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    /* Procedimiento almacenado sql de insert */
    $sql = "CALL formulario_insert('$nombre','$apellido','$email','$asunto')";

    /* Se ejecuta el procedimiento almacenado */
    $result = $conn->query($sql);

    $response = array();

    if ($result) {
        $response['success'] = "Mensaje enviado correctamente";
        exit(json_encode($response));
    } else {
        $response['error'] = "error" . $conn->error;
        exit(json_encode($response));
    }

    /* Se cierra la conexion */
    $conn->close();
}
