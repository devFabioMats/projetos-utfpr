import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ServidorHotel extends UnicastRemoteObject implements GerenciadorQuartos {
    private static final long serialVersionUID = 1L;
    
    private static final Map<Integer, QuartoInfo> TIPOS_QUARTOS = new HashMap<>();
    static {
        TIPOS_QUARTOS.put(0, new QuartoInfo(10, 100.00, "individual"));
        TIPOS_QUARTOS.put(1, new QuartoInfo(20, 150.00, "duplo"));
        TIPOS_QUARTOS.put(2, new QuartoInfo(5, 200.00, "duplo luxo"));
        TIPOS_QUARTOS.put(3, new QuartoInfo(3, 250.00, "triplo"));
        TIPOS_QUARTOS.put(4, new QuartoInfo(2, 300.00, "quádruplo"));
    }
    
    private Map<Integer, Integer> quartosDisponiveis;
    private List<String> listaHospedes;
    
    protected ServidorHotel() throws RemoteException {
        super();
        quartosDisponiveis = new HashMap<>();
        for (Map.Entry<Integer, QuartoInfo> entry : TIPOS_QUARTOS.entrySet()) {
            quartosDisponiveis.put(entry.getKey(), entry.getValue().quantidade);
        }
        listaHospedes = new ArrayList<>();
    }
    
    @Override
    public String listagem() throws RemoteException {
        StringBuilder sb = new StringBuilder();
        sb.append("=== Quartos Disponíveis ===\n");
        
        for (Map.Entry<Integer, QuartoInfo> entry : TIPOS_QUARTOS.entrySet()) {
            int tipo = entry.getKey();
            QuartoInfo info = entry.getValue();
            int disponiveis = quartosDisponiveis.get(tipo);
            
            sb.append(String.format("Tipo %d - %s quartos %s (R$ %.2f): %d disponíveis\n",
                    tipo, info.quantidade, info.descricao, info.preco, disponiveis));
        }
        
        return sb.toString();
    }
    
    @Override
    public boolean reserva(int tipoQuarto, String nomeHospede) throws RemoteException {
        if (!TIPOS_QUARTOS.containsKey(tipoQuarto)) {
            return false;
        }
        
        int disponiveis = quartosDisponiveis.get(tipoQuarto);
        if (disponiveis <= 0) {
            return false;
        }
        
        quartosDisponiveis.put(tipoQuarto, disponiveis - 1);
        listaHospedes.add(nomeHospede);
        System.out.println("Reserva feita pra " + nomeHospede + " no quarto tipo " + tipoQuarto);
        return true;
    }
    
    @Override
    public List<String> hospedes() throws RemoteException {
        return new ArrayList<>(listaHospedes);
    }
    
    private static class QuartoInfo {
        final int quantidade;
        final double preco;
        final String descricao;
        
        QuartoInfo(int quantidade, double preco, String descricao) {
            this.quantidade = quantidade;
            this.preco = preco;
            this.descricao = descricao;
        }
    }
    
    public static void main(String[] args) {
        try {
            ServidorHotel servidor = new ServidorHotel();
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.rebind("GerenciadorQuartos", servidor);
            
            System.out.println("Servidor rodando! Hotel aberto pra reservas :)");
            
        } catch (RemoteException e) {
            System.out.println("Deu ruim no servidor: " + e.getMessage());
            e.printStackTrace();
        }
    }
}