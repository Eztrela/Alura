<?php

$peso = 78;
$altura = 1.78;

$imc = $peso / $altura**2;

if($imc < 18.5){
    echo "seu imc é $imc, e voce esta na faixa de Magreza" . PHP_EOL;
}else if($imc < 24.9){
    echo "seu imc é $imc, e voce esta na faixa Normal" . PHP_EOL;
}else if($imc < 30){
    echo "seu imc é $imc, e voce esta na faixa de Sobrepeso" . PHP_EOL;
}else{
    echo "seu imc é $imc, e voce esta na faixa de Obesidade" . PHP_EOL;
}