<?php

include_once './config.php';

/* Se valida si existen las variables POST */

if (isset($_POST['Username']) && isset($_POST['Password'])) {

    /* Se asignan las variables */
    /* Contraseña encriptada mediante función hash */
    /* Metodo de encriptación: 'sha512' */

    $username = $_POST['Username'];
    $password = hash('sha512', $_POST['Password']);

    /* Se crea un array */
    $response = array();

    /* Se valida si los campos están vacios*/

    if ($username == '' || $password == '') {
        $response['success'] = "false";
        $response['message'] = "Por favor, rellena todos los campos";
        exit(json_encode($response));
    }

    /* consulta sql para verificar si existe un usuario con el nombre y contraseña ingresados */
    $sql = "SELECT * FROM `Usuarios` WHERE `Username` = '$username' AND `password` = '$password'";

    /* Se ejecuta la consulta */
    $result = $conn->query($sql);

    /* Se almacena la consulta en un array asociativo*/
    $fila = mysqli_fetch_object($result);

    /* Indices */
    /* 'success' indica el estado de la condición */
    /* 'message' indica el mensaje a mostrar (será recibido con JS) */

    if ($result->num_rows > 0) {

        /* Si existe mas de una fila, o sea hay existencias */
        /* Se inicia una sesión */

        session_start();

        /* Se asignan las variables de sesión necesarias */
        /* Admin se obtiene del array que contiene la fila de la consulta sql */
        /* Username se obtiene a través de la variable POST ingresada*/

        $_SESSION['Username'] = $username;
        $_SESSION['Admin'] = $fila->Admin;
        $Admin = $_SESSION['Admin'];

        /* Si el valor de la variable $Admin es 1, se incluye el acceso a la url "admin.php" */

        /* Se codifica el mensaje de estado en 'success' */

        $response['success'] = "true";
        exit(json_encode($response));

        /* Si no existen filas, o sea no hay coincidencias */
        /* Se codifica el mensaje de estado en false y un mensaje que indica lo sucedido */
    } else if ($result->num_rows == 0) {
        $response['success'] = "false";
        $response['message'] = "Datos de sesión incorrectos";
        exit(json_encode($response));
    }
}

$conn->close();
