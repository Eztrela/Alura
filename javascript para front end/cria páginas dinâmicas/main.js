function tocaSom(idTecla){
    document.querySelector(idTecla).play();
}


// const tecla_pom = document.querySelector('.tecla_pom');
// tecla_pom.addEventListener("click", () =>{tocaSom('#som_tecla_pom')} );

// tocaSom('#som_tecla_pom');
// tocaSom('#som_tecla_clap');

const teclas = document.querySelectorAll('.tecla');
console.log(teclas);

for (let i = 0; i < teclas.length; i++){
    const tecla = teclas[i];
    const instrumento = teclas[i].classList[1];
    const idAudio = `#som_${instrumento}`;
    tecla.addEventListener("click", () =>{tocaSom(idAudio)} );
}
