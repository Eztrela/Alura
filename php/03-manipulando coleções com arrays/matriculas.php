<?php

$alunos2021 = [
    'Ana' ,
    'Joao' ,
    'Maria' ,
    'Roberto' ,
    'Vinicius',
];

$novosAlunos = [
    'Patricia',
    'Nico',

];

//junta 2 arrays, é possivel tb usar o operador '+' para esta operação porém ele nao sobrescreve as chaves q ja existirem
//$alunos2022 = array_merge($alunos2021, $novosAlunos);

$alunos2022 = [...$alunos2021, ...$novosAlunos];
array_push($alunos2022, 'Alice', 'Carlos', 'Pedro');
$alunos2022[] = 'Luiz';
var_dump($alunos2022);


//spread operator('...') permite passar varios parametros do mesmo tipo para uma função
/*function funcao(array ...$alunos){
}

funcao([], [], [], []);

//unpack operator (...$array) 
function funcao2(int $a, int $b, int $c){

}

funcao(...[1,2,3]);

*/