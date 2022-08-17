<?php
//etiqueta de inicio

$bool = array(1, 0);
//asignacion de variable $bool (True, False)

//Negación
echo "Negación:\np\t~p\n";
foreach ($bool as $p) {
    $P = !$p;
    //ciclo for
    //comprueba los valores del arreglo
    echo "$p\t$P\n";
    //se muestran los valores finales por pantalla
}
//Conjunción
echo "\nConjunción:\np AND q\n";
foreach ($bool as $p) {
    foreach ($bool as $q) {
        $P = $p && $q;
        //comprueba los valores del arreglo
        echo "$p\t$q\t$P\n";
        //se muestran los valores finales por pantalla
    }
}
//Disyunción inclusiva
echo "\nDisyunción inclusiva:\np OR q\n";
foreach ($bool as $p) {
    foreach ($bool as $q) {
        $P = $p || $q;
        //comprueba los valores del arreglo
        echo "$p\t$q\t$P\n";
        //se muestran los valores finales por pantalla
    }
}
//Disyunción exclusiva
echo "\nDisyunción exclusiva:\np XOR q\n";
foreach ($bool as $p) {
    foreach ($bool as $q) {
        $P = $p != $q;
        //comprueba los valores del arreglo
        echo "$p\t$q\t$P\n";
        //se muestran los valores finales por pantalla
    }
}
// Condicional
echo "\nCondicional:\np -> q\n";
foreach ($bool as $p) {
    foreach ($bool as $q) {
        $P = !($p) || $q;
        //comprueba los valores del arreglo
        echo "$p\t$q\t$P\n";
        //se muestran los valores finales por pantalla
    }
}
// Bicondicional
echo "\nBicondicional:\np <-> q\n";
foreach ($bool as $p) {
    foreach ($bool as $q) {
        $P = $p == $q;
        //comprueba los valores del arreglo
        echo "$p\t$q\t$P\n";
        //se muestran los valores finales por pantalla
    }
}
//etiqueta de cierre
?>
