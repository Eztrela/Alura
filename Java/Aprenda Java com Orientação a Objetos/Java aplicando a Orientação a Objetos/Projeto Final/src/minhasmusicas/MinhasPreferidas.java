package minhasmusicas;

public class MinhasPreferidas {
    public void inclui(Audio audio){
        if(audio.getClassificacao() >= 8)
            System.out.println(audio.getTitulo() + " é considerado sucesso absoluto");
        else
            System.out.println(audio.getTitulo() + " Também é um dos que todo mundo esta curtindo");
    }
}
