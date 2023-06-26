package minhasmusicas;

public class Audio {
    private String titulo;
    private int totalReproducoes;
    private int curtidas;
    private double classificacao;

    public Audio(String titulo){
        this.titulo = titulo;
        this.totalReproducoes = 0;
        this.curtidas = 0;
        this.classificacao = 0;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public int getTotalReproducoes() {
        return totalReproducoes;
    }

    public int getCurtidas() {
        return curtidas;
    }

    public double getClassificacao() {
        return classificacao;
    }

    public void curtir(){
        this.curtidas++;
    }

    public void reproduz(){
        this.totalReproducoes++;
    }
}
