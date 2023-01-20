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
}

?>

<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./css/Home.css">
    <link rel="stylesheet" href="./css/nav.css">
    <link rel="stylesheet" href="./css/footer.css">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
    <link rel="icon" href="./img/Logo.png">
    <title>Defender - Home</title>
</head>

<body>
    <header class="header">
        <nav class="nav">
            <ul class="navlogo">
                <li><img id="logo" src="./img/Logo.png" alt="No Logo"></li>
                <li><a class="logotxt">Defender</a></li>
            </ul>
            <ul class="nav-buttons">

                <?php if ($_SESSION['Admin'] == 1) {
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

        <h1>Un antivirus gratuito, seguro, libre y multiplataforma</h1>
        <hr><br>

        <article class="article">

            <section class="imgL">
                <img src="./img/imgV.png" alt="" class="imagen">
            </section>

            <section class="t-cont">
                <p class="text">Defender es un antivirus gratuito por lo que no deberás preocuparte por pagos y
                    licencias para poder usarlo. Defender es un antivirus seguro, ya que no recopila datos personales de los usuarios y no tiene acceso a la cámara, micrófono o gps.
                    Defender es un antivirus libre, ya que su código fuente es abierto y se puede modificar a voluntad. <br><br>
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                    Ex autem molestias perspiciatis obcaecati omnis odit iste laborum nostrum dolor error, et,
                    qui facere officiis quas eaque dolores maxime enim voluptatibus odio libero eligendi nihil
                    laudantium neque assumenda. Ea tempora quisquam necessitatibus maiores ex incidunt quod nobis saepe
                    aliquid ab modi repudiandae sit quae dolore omnis, iusto eos fugiat possimus deserunt, reprehenderit
                    provident rem qui. Quis cumque harum eius ratione aperiam, officia voluptas vitae unde ad aliquid eaque
                    tempore quaerat porro debitis veritatis repellendus, quae ut sequi mollitia odio voluptatibus. Debitis cum
                    dignissimos inventore sint eum reprehenderit aperiam totam, doloremque, esse perferendis sunt nobis accusantium,
                    eligendi iste molestias illum exercitationem ut. Non iste harum, aut consequuntur, quia perspiciatis facilis numquam,
                    iusto ratione ad animi pariatur esse perferendis laudantium totam sint maxime aliquid culpa eum! Pariatur obcaecati magni
                    minus dicta, error illo ipsam porro tempora unde quis quisquam maiores eligendi repellendus mollitia placeat architecto
                    provident, modi voluptatibus voluptatem, reiciendis id. Enim quae, saepe laboriosam quaerat quod itaque molestias ab
                    adipisci possimus ex sequi veniam voluptas, reiciendis dicta, voluptatum accusantium? Animi obcaecati, magnam
                    reprehenderit recusandae deserunt optio labore voluptatibus dolorum est id qui fuga rem cumque aliquid omnis pariatur.
                    Rerum quaerat quas laboriosam.
                </p>

            </section>

            <section class="t-cont">
                <p class="text">Defender es un antivirus seguro, ya que cuenta con un sistema de protección contra
                    virus, spyware, rootkits, troyanos, gusanos, etc. <br><br> Además trabajamos en base a tus reportes, cualquier nueva amenaza será abordada de la manera mas minuciosa posible. <br><br>
                    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Impedit, rem! Provident odit cumque voluptates natus error sunt! Quaerat commodi optio cum molestiae dolor obcaecati quam ea, a at voluptatem! Quidem in, quaerat autem ipsa rerum ipsam commodi culpa sint et dolor saepe quis iure est, facilis molestias modi necessitatibus voluptates veritatis laudantium quas accusantium earum odio repellat placeat? Reiciendis blanditiis quae eaque aliquam, explicabo adipisci est qui amet! Ratione incidunt maxime molestiae temporibus quia aspernatur repellat voluptate sunt earum architecto, culpa inventore. Ea est magni facere totam commodi! Libero illum voluptas excepturi sequi porro et, inventore alias voluptatibus maiores dicta?

                </p>

            </section>

            <section class="imgR">
                <img src="./img/imgIII.png" alt="" class="imagen">
            </section>

            <section class="imgL">
                <img src="./img/imgV.png" alt="" class="imagen">
            </section>

            <section class="t-cont">
                <p class="text">Defender es un antivirus libre, ya que puedes descargarlo y usarlo sin ningún tipo de
                    restricción. <br><br>
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Magni, beatae ipsam fugit et optio sequi doloribus saepe nostrum hic ad eveniet odit quaerat deserunt soluta perspiciatis, a harum officia magnam, dolorem rem quam. Deleniti minima maxime iste in consequatur similique assumenda sint? Cumque ducimus deserunt quaerat distinctio molestiae possimus quia. Vero repellat debitis magnam asperiores perferendis nihil consectetur earum reiciendis possimus dolore reprehenderit facere nesciunt commodi voluptatem dicta unde alias, rerum et, porro inventore hic quis! Explicabo recusandae repellendus aperiam cupiditate nostrum provident nihil consectetur, architecto repellat a tempora maxime laudantium debitis deserunt nam cumque eos similique dolor quibusdam, libero animi soluta minus, totam reprehenderit. Exercitationem, vel rerum! Ex molestiae laborum architecto? Hic voluptas officiis, numquam voluptatum magni culpa vero esse, possimus velit maxime optio dignissimos porro natus, blanditiis fugiat commodi ex. Dolor obcaecati ex maxime mollitia libero ullam veritatis non eius harum recusandae perferendis, delectus odit. Ducimus, est. Consequatur amet ipsum aliquam facilis aut necessitatibus expedita ducimus magni quibusdam assumenda, unde explicabo! Eius, hic reiciendis saepe harum minus fuga debitis magnam ipsam accusamus veritatis in nobis natus velit? Ad commodi in aperiam eligendi natus, nostrum unde error autem rerum facilis doloribus ipsam obcaecati perferendis inventore consequuntur fugiat quas necessitatibus!
                </p>
            </section>

            <section class="t-cont">
                <p class="text">
                    Defender es un antivirus multiplataforma, ya que puedes usarlo en Windows, Linux y MacOS. <br><br>
                    Lorem ipsum dolor sit, amet consectetur adipisicing elit. Nobis, soluta saepe velit repudiandae illum sunt tempore in, repellat qui, eos magnam dicta possimus odio facere tenetur unde! Minus ducimus incidunt dolorum earum ratione excepturi, neque aliquid, sapiente fugiat hic non fuga distinctio officiis optio reprehenderit quo quia natus error deserunt voluptatibus? Quisquam nulla voluptatum tenetur praesentium, tempora illo dolorum dolorem tempore voluptatibus ducimus, fuga suscipit accusamus sed aut ipsum rem omnis quibusdam, doloremque architecto enim cumque exercitationem. Consectetur eligendi accusamus, distinctio eius sit esse itaque numquam tempora quidem ducimus facilis sed vero minus voluptates fuga. In, adipisci mollitia! Accusantium, molestiae.
                </p>
            </section>

            <section class="imgR">
                <img src="./img/imgIII.png" alt="" class="imagen">
            </section>

        </article><br>
        <hr>

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
                <li><a href="teitter.com"></a><img src="./img/twitter.png" alt=""></li>
            </ul>
        </nav>
    </footer>

</body>

</html>