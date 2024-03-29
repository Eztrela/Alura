package br.com.alura.screenmatch.principal;

import br.com.alura.screenmatch.excecao.ErroDeConversaoDeAnoException;
import br.com.alura.screenmatch.modelos.Titulo;
import br.com.alura.screenmatch.modelos.TituloOMDB;
import com.google.gson.FieldNamingPolicy;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Scanner;

public class PrincipalComBusca {
    public static void main(String[] args) throws IOException, InterruptedException {
        Scanner leitura = new Scanner(System.in);
        System.out.println("Digite um nome de um filme");
        var busca = leitura.nextLine();
        String endereco = "http://www.omdbapi.com/?t=" + busca.replace(" ", "+") + "&apikey=af721913";
        try {
            HttpClient client = HttpClient.newHttpClient();
            HttpRequest request = HttpRequest.newBuilder().uri(URI.create(endereco)).build();
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            String json = response.body();
            Gson gson = new GsonBuilder().setFieldNamingPolicy(FieldNamingPolicy.UPPER_CAMEL_CASE).create();
            TituloOMDB meuTituloOmdb = gson.fromJson(json, TituloOMDB.class);

            Titulo meuTitulo = new Titulo(meuTituloOmdb);
            System.out.println(meuTitulo);
        } catch (NumberFormatException e) {
            System.out.println("Aconteceu um erro");
            System.out.println(e.getMessage());
        } catch (IllegalArgumentException e) {
            System.out.println("Algum erro de Argumento na busca, verifique o endereço");
        } catch (ErroDeConversaoDeAnoException e) {
            System.out.println(e.getMessage());
        }
    }
}
