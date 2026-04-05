namespace ProgramacaoOO.Domain;

public class Usuario
{
    public long Id { get; }
    public string Nome { get; }
    public string Email { get; }

    public Usuario(long id, string nome, string email)
    {
        Id = id;
        Nome = nome;
        Email = email;
    }

    public Pedido FazerPedido(long pedidoId)
    {
        return new Pedido(pedidoId, this);
    }
}
