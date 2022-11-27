<?php

/* Para que se pueda destruir la sesión es necesario que exista sesión_start() */

session_start();

/* Se destruye la sesión existente y se redirecciona a index */

session_destroy();
header("Location:../index.html");
