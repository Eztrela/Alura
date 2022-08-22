<?php

$notas = [
    'Ana' => 10,
    'Joao' => 8,
    'Maria' => 9,
    'Roberto' => 10,
    'Vinicius' => '6',

];

$array = [
    0 => 'um',
    1 => 'dois',
    2 => 'tres'
];


//sort reverso
//rsort($notas);
//var_dump($notas);

//sort associativo reverso
arsort($notas);
var_dump($notas);

//sort pelas keys existe tb o krsort()
ksort($notas);
var_dump($notas);

// tudo isso pode ser utilizado tb no usort() ex: uksort() uasort()...


if (is_array($notas)){
    echo 'sim, é um array' . PHP_EOL;
}

// verifica se o array segue os indices crescentes e com acrescimo de um a um ex: 0,1,2,3,4,5,6...
var_dump(array_is_list($array));

// verifica se chave existe no array
var_dump(array_key_exists('Vinicius', $notas));

//isset verifica se a chave existe e o valor dela é diferente de nulo

var_dump(isset($notas['Ana']));

//verifica se o valor existe no array, strict == bool para forçar a comparar o valor eo tipo usando o operador ===
var_dump(in_array(6, $notas, true));

//busca por um valor e retorna a chave referente a ele para o primeiro caso, strict == bool para forçar a comparar o valor eo tipo usando o operador ===
echo array_search(10, $notas ,true);

