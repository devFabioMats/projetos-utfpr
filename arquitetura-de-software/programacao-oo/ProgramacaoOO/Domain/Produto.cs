namespace ProgramacaoOO.Domain;

public class Produto
{
    public long Id { get; }
    public string Nome { get; }
    public decimal PrecoAtual { get; }
    public int Estoque { get; private set; }

    public Produto(long id, string nome, decimal precoAtual, int estoque)
    {
        Id = id;
        Nome = nome;
        PrecoAtual = precoAtual;
        Estoque = estoque;
    }

    public void ReduzirEstoque(int quantidade)
    {
        if (quantidade <= 0)
        {
            throw new ArgumentException("Quantidade deve ser maior que zero.");
        }

        if (quantidade > Estoque)
        {
            throw new ArgumentException("Estoque insuficiente.");
        }

        Estoque -= quantidade;
    }
}
