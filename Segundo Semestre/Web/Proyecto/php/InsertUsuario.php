<?php

/* Enlaza el archivo config.php */
/* Contiene la información relacionada a la DB */

include_once './config.php';

/* Se obtienen los valores mediante método POST del formulario html */
/* Contraseña se encripta mediante función hash con método 'sha512' */
/* Variable admin = 0, ya que por defecto el nuevo usuario no será administrador */

$Urut = $_POST['rut'];
$Username = $_POST['newuser'];
$Uemail = $_POST['newemail'];
$Upassword = hash('sha512', $_POST['newpass']);
$admin = 0;

/* Función que valida mediante función integrada 'empty' y operadores lógicos si alguna de las variables es nula/vacia*/

function validarvaciouser($Urut, $Username, $Uemail, $Upassword)
{
    if (empty($Urut) || empty($Username) || empty($Uemail) || empty($Upassword)) {
        return false;
    } else {
        return true;
    }
}

/* Función que valida la longitud de caracteres de las variables ingresadas */
/* compara valores uno a uno con las longitudes aceptadas por la BD ($num) */

function validaruserlong($Urut, $Username, $Uemail, $Upassword)
{
    $num = array(9, 25, 50, 100000);
    $lista = array($Urut, $Username, $Uemail, $Upassword);

    for ($i = 0; $i < count($lista); $i++) {
        if (strlen($lista[$i]) > $num[$i]) {
            return false;
        } else {
            return true;
        }
    }
}

/* Función que valida si el mail ingresado corresponde a uno real */
/* Similiar a expresiones regulares de JS */

function validarmail($Uemail)
{
    if (filter_var($Uemail, FILTER_VALIDATE_EMAIL)) {
        return true;
    } else {
        return false;
    }
}

/* Esta función valida la validez de todas las funciones anteriores */

function validaruser($Urut, $Username, $Uemail, $Upassword)
{
    if (
        validarvaciouser($Urut, $Username, $Uemail, $Upassword)
        && validaruserlong($Urut, $Username, $Uemail, $Upassword)
        && validarmail($Uemail)
    ) {
        return true;
    } else {
        return false;
    }
}

/* Función que Ejecuta consulta INSERT en BD */
/* Recibe los datos $POST de HTML y la conexion ($conn) directamente de 'config.php' */

/* $response */

/* A partir de esta función se hace uso de $response el cual es un array asociativo similar a Json */
/* con este array se envian mensajes de estado dependiendo del resultado de cada función */
/* estos estados seran detectador por JS y serán mostrados en forma de alertas o texto plano en la WEB. */

function InsertUser($Urut, $Username, $Uemail, $Upassword, $admin, $conn)
{

    $sql = "INSERT INTO `Usuarios`(`RUT`, `Username`, `email`, `password`, `Admin`) VALUES 
        ('$Urut','$Username','$Uemail','$Upassword','$admin')";

    $result = $conn->query($sql);
    $response = array();

    if ($result) {
        $response['status'] = "Te haz registrado correctamente";
        exit(json_encode($response));
        $conn->close();
    } else {
        $response['error'] = "error" . $conn->error;
        exit(json_encode($response));
    }
}

/* Función que valida si un usuario ya existe en la BD */
/* Mediante una consulta simple se verifica si el NomUsuario || RUT || Email existen */

function ValidateUserExist($Urut, $Username, $Uemail, $Upassword, $admin, $conn)
{
    $sql = "SELECT * FROM `Usuarios` WHERE `RUT` = '$Urut' OR `Username` = '$Username' OR `email` = '$Uemail'";
    $result = $conn->query($sql);
    $response = array();

    if ($result->num_rows > 0) {
        $response['status'] = "El usuario ya existe";
        exit(json_encode($response));
    } else {
        InsertUser($Urut, $Username, $Uemail, $Upassword, $admin, $conn);
    }
}

/* Si la validación general resulta correcta */
/* Se ejecuta la validación de existencias y posteriormente la inserción */

if (validaruser($Urut, $Username, $Uemail, $Upassword) == true) {

    ValidateUserExist($Urut, $Username, $Uemail, $Upassword, $admin, $conn);
}
