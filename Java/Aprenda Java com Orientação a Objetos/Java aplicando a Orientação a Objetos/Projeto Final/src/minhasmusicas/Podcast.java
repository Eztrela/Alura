package minhasmusicas;

public class Podcast extends Audio{
    private String host;
    private String descricao;
    public Podcast(String titulo,String host, String descricao){
        super(titulo);
        this.host=host;
        this.descricao = descricao;

    }

    public String getHost() {
        return host;
    }

    public void setHost(String host) {
        this.host = host;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    @Override
    public double getClassificacao() {
        if(this.getCurtidas() > 500)
            return 10;
        else
            return 8;
    }
}
