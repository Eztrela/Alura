<?php

$array = [
    1 => 'um',
    2 => 'dois',
    3 => 'tres',
];


$contador = 0;
foreach ($array as $numeral => $nomeNumero){
    echo "$numeral em português é: $nomeNumero" . PHP_EOL;
    $contador++;
}

echo "Total: " . count($array) . PHP_EOL;