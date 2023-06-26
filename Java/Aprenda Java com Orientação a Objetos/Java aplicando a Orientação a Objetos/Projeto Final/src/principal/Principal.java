package principal;

import minhasmusicas.MinhasPreferidas;
import minhasmusicas.Musica;
import minhasmusicas.Podcast;

public class Principal {
    public static void main(String[] args) {
        Musica minhaMusica = new Musica("forever","kiss");
        for (int i = 0; i < 1000; i++) {
            minhaMusica.reproduz();
        }
        for (int i = 0; i < 50; i++) {
            minhaMusica.curtir();
        }

        Podcast meuPodcast = new Podcast("BolhaDev","Marcus Mendes", "");

        for (int i = 0; i < 5000; i++) {
            meuPodcast.reproduz();
        }
        for (int i = 0; i < 1000; i++) {
            meuPodcast.curtir();
        }

        MinhasPreferidas preferidas = new MinhasPreferidas();
        preferidas.inclui(meuPodcast);
        preferidas.inclui(minhaMusica);

    }
}
