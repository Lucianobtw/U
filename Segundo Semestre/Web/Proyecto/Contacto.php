<?php

/* Se inicia la sesión */

session_start();

if (isset($_SESSION['Username']) && isset($_SESSION['Admin'])) {

    /* La variable $user contendrá la variable de sesión definida en Login.php */
    /* La variable contiene el nombre del usuario logeado */

    $user = $_SESSION['Username'];

    /* Si la variable de sesión esta vacia o es nula se redirecciona al index*/
    /* esto servirá para que cualquier persona que intente ingresar de manera directa por URL sea redireccionado */

    if ($user == null || $user = '') {
        header("Location:./index.html");
    }

    /* La variable de sesión admin viene asignada directamente de la validación de sesión SQL */
    /* Si se intenta acceder a esta URL y esta variable es 0 || vacia se redicionará al home*/

    $Admin = $_SESSION['Admin'];
}

?>

<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="./css/Contacto.css" />
    <link rel="stylesheet" href="./css/nav.css" />
    <link rel="stylesheet" href="./css/footer.css" />
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet" />
    <link rel="icon" href="./img/Logo.png" />
    <title>Defender - Contacto</title>
</head>

<body>
    <header class="header">
        <nav class="nav">
            <ul class="navlogo">
                <li><img id="logo" src="./img/Logo.png" alt="No Logo" /></li>
                <li><a class="logotxt">Defender</a></li>
            </ul>

            <ul class="nav-buttons">
                <?php if ($Admin == 1) {
                    echo '<li class="nav-button"><a href="./Admin.php">Set Up</a></li>';
                }
                ?>
                <li class="nav-button"><a href="./Home.php">Home</a></li>
                <li class="nav-button"><a href="./Productos.php">Products</a></li>
                <li class="nav-button"><a href="./Quienes.php">About us</a></li>
                <li class="nav-button"><a href="./Contacto.php">Support</a></li>
                <li class="nav-button"><a href="./php/Logout.php">Log Out</a></li>
            </ul>
        </nav>
    </header>

    <main class="container">
        <section class="flex-cont">
            <form id="formulario" class="formulario" method="post">
                <input type="text" class="input" name="Nombre" id="nombre" placeholder="Name" />
                <input type="text" class="input" name="Apellido" id="apellido" placeholder="Lastname" />
                <input type="text" class="input" name="email" id="email" placeholder="Email adress" />
                <input type="text" class="input" name="Asunto" id="asunto" placeholder="Your Message" />
                <input id="boton" name="submit" type="submit" value="Enviar datos" />
            </form>

            <div class="respuesta">
                <div class="respuesta-p" id="respuesta"></div>
            </div>
        </section>
    </main>
    <script src="./Javascript/InsertContacto.js"></script>
</body>

</html>