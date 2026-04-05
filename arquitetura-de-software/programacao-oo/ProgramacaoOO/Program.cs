using ProgramacaoOO.Domain;
using ProgramacaoOO.Service.Impl;

namespace ProgramacaoOO;

internal static class Program
{
    private static void Main()
    {
        var usuario = new Usuario(1, "Fabio", "fabio@email.com");

        var produto = new Produto(1, "Notebook", 3500.00m, 10);
        var item = new ItemPedido(1, 1, produto);

        var pedido = usuario.FazerPedido(1001);
        pedido.AdicionarItem(item);
        pedido.FecharPedido(new PagamentoPix(), new FreteCorreios());

        Console.WriteLine($"Pedido: {pedido.Id}");
        Console.WriteLine($"Status: {pedido.Status}");
        Console.WriteLine($"Subtotal: {pedido.CalcularSubTotal():C}");
        Console.WriteLine($"Frete: {pedido.ValorFrete:C}");
        Console.WriteLine($"Total: {pedido.ValorTotal:C}");
    }
}
