package minhasmusicas;

public class Musica extends Audio{
    private String album;
    private String cantor;
    private String genero;
    public Musica(String titulo, String album){
        super(titulo);
        this.album = album;

    }

    public String getAlbum() {
        return album;
    }

    public void setAlbum(String album) {
        this.album = album;
    }

    @Override
    public double getClassificacao() {
        if(this.getTotalReproducoes() > 2000)
            return 10;
        else
            return 7;
    }
}
