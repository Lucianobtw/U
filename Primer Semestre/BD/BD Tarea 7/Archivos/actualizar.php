<?php

// Me conecto al motor de BD que corre en localhost.
// Ingreso el nombre y contraseña de usuario.
// Ingreso el nombre de la base de datos.

 $bd = mysqli_connect("localhost","root", "","zapatillasdb");

 if(!$bd) echo "Error en la conexión";
 
//Recibo los parametros ingresados en el formulario html y los transformo a variables php ($)

  $ID  = $_GET["IDProducto"];
  $porc =  $_GET["porcentaje"];

//Realizo la consulta SQL (Call UpdatePrecio)
$respuesta = mysqli_query($bd, "Call UpdatePrecio($ID, $porc)");
 

//Muestro un mensaje si todo estuvo bien.

if($respuesta) {
   echo "EL precio de la zapatilla ID: $ID ha sido actualizado.";
   }
else
   echo "Ocurrió un error";
?>