public class Audio {
    private String titulo;
    private int duracao;
    private int totalReproducoes;
    private int curtidas;
    private double classificacao;

    public Audio(String titulo,int duracao){
        this.titulo = titulo;
        this.duracao = duracao;
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

    public int getDuracao() {
        return duracao;
    }

    public void setDuracao(int duracao) {
        this.duracao = duracao;
    }

    public void curtir(){
        this.curtidas++;
    }
}
