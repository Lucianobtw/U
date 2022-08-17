<?php

// Me conecto al motor de BD que corre en localhost.
// Ingreso el nombre y contraseña de usuario.
// Ingreso el nombre de la base de datos.

 $bd = mysqli_connect("localhost","root", "","zapatillasdb");

 if(!$bd) echo "Error en la conexión";

//Recibo los parametros ingresados en el formulario html y los transformo a variables php ($)

  $ID = $_GET["IDProducto"];
  $Mod = $_GET["Modelo"];
  $Stock = $_GET["Stock"];
  $Mat = $_GET["Material"];
  $Precio = $_GET["Precio"];
  $Talla = $_GET["Talla"];

//Realizo la consulta SQL (Call InserZapatilla)

$respuesta = mysqli_query($bd, "Call InsertZapatilla($ID,'$Mod',$Stock,'$Mat',$Precio,'$Talla')");

//Muestro un mensaje si todo estuvo bien.

if($respuesta) {
   echo "Se ha añadido la zapatilla de ID: $ID";
   }
else
   echo "Ocurrió un error";
?>
