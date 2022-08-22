<?php

$notasBimestre1 = [
    'Ana' => 10,
    'Joao' => 8,
    'Maria' => 9,
    'Roberto' => 10,
    'Vinicius' => 6,

];

$notasBimestre2 = [
    'Ana' => 10,
    'Joao' => 8,
    'Maria' => 9,
    

];



//retorna os elementos q estao em 1 dos arrays mas nao esta no outro
$alunosFaltantes = array_diff_key($notasBimestre1, $notasBimestre2);
$nomesAlunos = array_keys($alunosFaltantes);
$notasAlunos = array_values($alunosFaltantes);

var_dump(array_combine($notasAlunos, $nomesAlunos));
var_dump(array_flip($alunosFaltantes));