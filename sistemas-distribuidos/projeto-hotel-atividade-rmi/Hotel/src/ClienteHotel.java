import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.List;
import java.util.Scanner;

public class ClienteHotel {
    private static GerenciadorQuartos gerenciador;
    
    public static void main(String[] args) {
        try {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            gerenciador = (GerenciadorQuartos) registry.lookup("GerenciadorQuartos");
            
            System.out.println("Conectado no hotel! Bora fazer umas reservas");
            menuInterativo();
            
        } catch (Exception e) {
            System.out.println("Não conseguiu conectar no servidor: " + e.getMessage());
            e.printStackTrace();
        }
    }
    
    private static void menuInterativo() {
        Scanner scanner = new Scanner(System.in);
        String comando;
        
        System.out.println("=== Sistema de Reservas de Hotel ===");
        System.out.println("Comandos disponíveis:");
        System.out.println("listagem - mostra quartos disponíveis");
        System.out.println("reserva <tipo> <nome> - faz uma reserva");
        System.out.println("hospedes - lista todos os hóspedes");
        System.out.println("sair - encerra o programa");
        
        while (true) {
            try {
                System.out.print("\nDigite um comando: ");
                comando = scanner.nextLine().trim();
                
                if (comando.equals("sair")) {
                    break;
                }
                
                processarComando(comando);
                
            } catch (Exception e) {
                System.out.println("Algo deu errado: " + e.getMessage());
            }
        }
        
        scanner.close();
        System.out.println("Tchau! Até a próxima :)");
    }
    
    private static void processarComando(String comando) throws Exception {
        String[] partes = comando.split(" ");
        String operacao = partes[0].toLowerCase();
        
        switch (operacao) {
            case "listagem":
                System.out.println(gerenciador.listagem());
                break;
                
            case "reserva":
                if (partes.length < 3) {
                    System.out.println("Uso: reserva <tipo> <nome>");
                    return;
                }
                try {
                    int tipo = Integer.parseInt(partes[1]);
                    // Junta todas as partes restantes como nome
                    String nome = String.join(" ", java.util.Arrays.copyOfRange(partes, 2, partes.length));
                    
                    boolean sucesso = gerenciador.reserva(tipo, nome);
                    if (sucesso) {
                        System.out.println("Oba! Reserva feita pra " + nome + " :D");
                    } else {
                        System.out.println("Eita, não rolou a reserva... deve tá lotado ou tipo errado");
                    }
                } catch (NumberFormatException e) {
                    System.out.println("Ei, o tipo tem que ser número de 0 a 4!");
                }
                break;
                
            case "hospedes":
                List<String> hospedes = gerenciador.hospedes();
                System.out.println("\n=== Galera que tá hospedada ===");
                if (hospedes.isEmpty()) {
                    System.out.println("Hotel vazio ainda :(");
                } else {
                    for (int i = 0; i < hospedes.size(); i++) {
                        System.out.println((i + 1) + ". " + hospedes.get(i));
                    }
                }
                break;
                
            default:
                System.out.println("Comando errado aí... tenta 'listagem', 'reserva <tipo> <nome>' ou 'hospedes'");
        }
    }
}