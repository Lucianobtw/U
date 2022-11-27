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
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta class="e-input" name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Administrador - Defender</title>
    <link rel="icon" href="./img/Logo.png" />
    <link rel="stylesheet" href="./css/nav.css" />
    <link rel="stylesheet" href="./css/Admin.css" />
    <link rel="stylesheet" href="./css/footer.css" />
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

    <main>
        <article>
            <section class="pagetitle">
                <h1 class="UCT" id="Titulo">Administrar Portal de Noticias</h1>
                <br />
                <hr /><br />
            </section>

            <section class="grid">
                <ul class="contactpanel" id="left"></ul>

                <section class="contactpanel" id="right">
                    <form class="fright" id="fright" method="post">
                        <label for="ID Solicitud">ID (No editable)</label>
                        <input type="text" class="e-input" name="ID" id="ID" />
                        <label for="Nombre">Primer Nombre</label>
                        <input type="text" class="e-input" name="EditNombre" id="EditNombre" />
                        <label for="Apellido">Primer Apellido</label>
                        <input type="text" class="e-input" name="EditApellido" id="EditApellido" />
                        <label for="Email">Email</label>
                        <input type="text" class="e-input" name="EditEmail" id="EditEmail" />
                        <label for="Mensaje">Mensaje</label>
                        <input type="text" class="e-input" name="EditMensaje" id="EditMensaje">
                    </form>

                    <div class="e-botones-master">
                        <input id="e-update" class="e-btn" type="submit" value="Editar Solicitud" />
                        <input id="e-delete" class="e-btn" type="submit" value="Eliminar Solicitud" />
                        <input id="e-email" class="e-btn" type="submit" value="Responder via email" />
                    </div>

                </section>
            </section>


        </article>
    </main>

    <footer class="footer">
        <nav class="footer-nav">
            <ul class="footer-text">
                <li>Defender</li>
                <li>Copyright</li>
            </ul>

            <ul class="links">
                <li>
                    <a href="facebook.com"><img src="./img/facebook.png" alt="" /></a>
                </li>
                <li>
                    <a href="instagram.com"><img src="./img/instagram.png" alt="" /></a>
                </li>
                <li> <a href="teitter.com"></a><img src="./img/twitter.png" alt="" /> </li>
            </ul>
        </nav>
    </footer>
    <script src="./Javascript/SelectContacto.js"></script>
</body>

</html>