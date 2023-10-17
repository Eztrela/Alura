import java.util.Random;
import java.util.Scanner;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Adivinhacao {
    public static void main(String[] args) {
        int sorteado = new Random().nextInt(100);
        Scanner leitor = new Scanner(System.in);
        for (int i = 0; i < 5; i++) {
            int chute = leitor.nextInt();
            if (chute == sorteado){
                System.out.println("Voce acertou o numero");
                acertou = true;
                break;
            }else if(chute < sorteado){
                System.out.println("O chute é menor que o número sorteado");
            }else if (chute > sorteado){
                System.out.println("O chute é maior que o número sorteado");
            }
        }
        if(i == 5){
            System.out.println("Não conseguiu acertar o numero em 5 tentativas");
        }
    }
}