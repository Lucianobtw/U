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

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./css/Quienes.css">
    <link rel="stylesheet" href="./css/nav.css">
    <link rel="stylesheet" href="./css/footer.css">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
    <link rel="icon" href="./img/Logo.png">
    <title>Defender - Nosotros</title>

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

        <h1>Somos Defender</h1>
        <hr><br>

        <article class="article">

            <section>
                <img class="imagen" src="./img/timeline.png" alt="">
            </section>

            <section>
                <h2 class="Titulo" id="Titulo">Historia</h1>
                    <p class="t-history"> Como estudiantes de la carrera de Ingenieria civil informatica nos dimos cuenta de la necesidad de una empresa que brinde seguridad a las personas, por lo que decidimos crear Defender, una empresa que brinda seguridad a las personas, brindando un servicio de calidad y confianza, con el fin de que las personas se sientan seguras y acompañadas en todo momento. <br> <br>
                        Defender nace en el año 2022, como un proyecto del ramo de Desarrollo web.
                    </p>
            </section>

            <section class="Biografias">
                <h2 class="Titulo" id="Titulo">Equipo</h2>

                <div class="integrante">
                    <h3 class="nombres">Luciano Revillod</h3>
                    <p>Estudiante de Ingenieria civil informatica en la Universidad Catolica de Temuco. <br>
                        Edad: 19 años. <br>
                        Hobbies: Escuchar musica, ver series y peliculas.
                    </p>
                </div>
                <div class="integrante">

                    <h3 class="nombres">Nicolás Valenzuela</h3>
                    <p>Estudiante de Ingenieria civil informatica en la Universidad Catolica de Temuco <br>
                        Edad: 18 años <br>
                        Hobbies: Jugar videojuegos, escuchar musica, ver series y peliculas.
                    </p>
                </div>
            </section>

            <section class="fleximg">
                <img class="imagen" id="TeamImg" src="./img/Team.jpg" alt="">
            </section>

        </article><br>
        <hr><br>

    </main>

    <footer class="footer">

        <nav class="footer-nav">

            <ul class="footer-text">

                <li>Defender</li>
                <li>Copyright</li>
            </ul>

            <ul class="links">

                <li><a href="facebook.com"><img src="./img/facebook.png" alt=""></a></li>
                <li><a href="instagram.com"><img src="./img/instagram.png" alt=""></a></li>
                <li><a href="twitter.com"></a><img src="./img/twitter.png" alt=""></li>
            </ul>

        </nav>

    </footer>

</body>

</html>