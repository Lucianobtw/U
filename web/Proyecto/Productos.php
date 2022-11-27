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
    <link rel="stylesheet" href="./css/Productos.css" />
    <link rel="stylesheet" href="./css/nav.css" />
    <link rel="stylesheet" href="./css/footer.css" />
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet" />
    <link rel="icon" href="./img/Logo.png" />
    <title>Defender - Productos</title>
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
        <h1>En Defender tenemos multiples opciones que se acomodan a tus necesidades.</h1><br />
        <hr /><br />

        <article class="article">
            <section class="Productos" id="Productos">
                <img src="./img/imgIII.png" alt="" class="imagen" />
            </section>

            <section class="texto">
                <h2 class="Subtitulo">Productos</h2>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero commodi aliquam beatae, consectetur neque similique. Facere laboriosam ex est numquam quasi nisi eveniet, ut
                    autem, iste soluta aliquam sapiente, omnis qui ab culpa nobis aut saepe amet quaerat molestiae temporibus officiis. Eligendi soluta quidem temporibus velit in animi, cupiditate
                    accusantium sed culpa. Harum, tempore. Ut delectus dolorem illo modi nostrum illum reiciendis? Temporibus eligendi atque, quibusdam minus voluptas sed ipsum animi libero
                    labore. Rerum, quasi. Numquam, facere. Aspernatur obcaecati illo fugit ut, officia a iusto quis sequi sed, culpa, itaque rem distinctio consequatur deserunt nulla laudantium
                    officiis reiciendis ipsam voluptates earum aut sit neque. Laborum vel dolores odio quae ut accusamus harum quos officiis fuga. Architecto repudiandae nobis tenetur ipsum sit!
                    Iusto ex nemo ipsam laudantium quas! At veniam adipisci dignissimos quo voluptatum facere nihil minima corrupti aperiam molestiae, repudiandae, commodi deserunt harum ratione
                    ab cumque! Sapiente amet cupiditate laborum atque, totam expedita voluptates maxime officiis cum est vitae assumenda! Labore fugit minima vero in nemo quod pariatur odit
                    possimus praesentium, exercitationem, dolorem officia, a est corporis sed? Unde consequuntur modi asperiores quos aliquid adipisci aut perspiciatis dolore, non quo tempora
                    eius. Officia commodi nulla a, similique qui at obcaecati.</p>
            </section>

            <section class="tables">
                <h3>Disponibilidad en Sistemas operativos</h3>

                <table class="table">
                    <tr>
                        <th>OS</th>
                        <th>Nivel I</th>
                        <th>Nivel II</th>
                        <th>Nivel III</th>
                    </tr>
                    <tr>
                        <td>Windows</td>
                        <td><img src="./img/ticket.png" alt="Error de carga" class="ticket" /></td>
                        <td><img src="./img/ticket.png" alt="Error de carga" class="ticket" /></td>
                        <td><img src="./img/ticket.png" alt="Error de carga" class="ticket" /></td>
                    </tr>
                    <tr>
                        <td>Linux</td>
                        <td><img src="./img/X.png" alt="Error de carga" class="ticket" /></td>
                        <td><img src="./img/ticket.png" alt="Error de carga" class="ticket" /></td>
                        <td><img src="./img/ticket.png" alt="Error de carga" class="ticket" /></td>
                    </tr>
                    <tr>
                        <td>Mac OS</td>
                        <td><img src="./img/X.png" alt="Error de carga" class="ticket" /></td>
                        <td><img src="./img/X.png" alt="Error de carga" class="ticket" /></td>
                        <td><img src="./img/ticket.png" alt="Error de carga" class="ticket" /></td>
                    </tr>
                </table>
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
                <li><a href="facebook.com"><img src="./img/facebook.png" alt="" /></a></li>
                <li><a href="instagram.com"><img src="./img/instagram.png" alt="" /></a></li>
                <li><a href="teitter.com"></a><img src="./img/twitter.png" alt="" /></li>
            </ul>
        </nav>
    </footer>

</body>

</html>