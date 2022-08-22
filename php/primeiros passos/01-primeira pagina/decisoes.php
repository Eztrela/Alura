<?php

$idade = 17;
$numeroDePessoas = 2;

echo "Voce so pode entrar se tiver mais de 18 anos" . PHP_EOL;

if ($idade >= 18){
    echo "Voce tem $idade anos." . PHP_EOL;
    echo "Pode entrar";
}elseif($idade >= 16 and $numeroDePessoas > 1){
    echo "Voce tem $idade anos, esta acompanhado(a), entao voce pode entrar";
}else{
    echo "Voce tem $idade anos. Voce nao pode entrar";
}