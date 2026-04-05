namespace ProgramacaoOO.Domain;

public class ItemPedido
{
    public long Id { get; }
    public int Quantidade { get; }
    public decimal PrecoUnitario { get; }
    public Produto Produto { get; }

    public ItemPedido(long id, int quantidade, Produto produto)
    {
        Produto = produto ?? throw new ArgumentException("Produto nao pode ser nulo.");

        if (quantidade <= 0)
        {
            throw new ArgumentException("Quantidade deve ser maior que zero.");
        }

        Id = id;
        Quantidade = quantidade;
        PrecoUnitario = produto.PrecoAtual;
    }

    public decimal CalcularTotalItem()
    {
        return PrecoUnitario * Quantidade;
    }
}
