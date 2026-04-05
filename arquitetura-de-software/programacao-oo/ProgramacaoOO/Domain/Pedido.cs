using ProgramacaoOO.Service;

namespace ProgramacaoOO.Domain;

public class Pedido
{
    private readonly List<ItemPedido> _itens = new();

    public long Id { get; }
    public DateTime DataCriacao { get; }
    public StatusPedido Status { get; private set; }
    public decimal ValorFrete { get; private set; }
    public decimal ValorTotal { get; private set; }
    public Usuario Usuario { get; }
    public IReadOnlyList<ItemPedido> Itens => _itens.AsReadOnly();

    public Pedido(long id, Usuario usuario)
    {
        Usuario = usuario ?? throw new ArgumentException("Usuario nao pode ser nulo.");

        Id = id;
        DataCriacao = DateTime.Now;
        Status = StatusPedido.AguardandoPagamento;
        ValorFrete = 0m;
        ValorTotal = 0m;
    }

    public void AdicionarItem(ItemPedido item)
    {
        if (item is null)
        {
            throw new ArgumentException("Item nao pode ser nulo.");
        }

        _itens.Add(item);
    }

    public decimal CalcularSubTotal()
    {
        return _itens.Sum(i => i.CalcularTotalItem());
    }

    public void FecharPedido(IProcessadorPagamento pag, ICalculadorFrete frete)
    {
        if (pag is null || frete is null)
        {
            throw new ArgumentException("Dependencias de pagamento e frete sao obrigatorias.");
        }

        if (_itens.Count == 0)
        {
            throw new InvalidOperationException("Nao e possivel fechar pedido sem itens.");
        }

        ValorFrete = frete.CalcularFrete(this);
        ValorTotal = CalcularSubTotal() + ValorFrete;

        var pagamentoOk = pag.Processar(this);
        Status = pagamentoOk ? StatusPedido.Pago : StatusPedido.AguardandoPagamento;
    }
}
