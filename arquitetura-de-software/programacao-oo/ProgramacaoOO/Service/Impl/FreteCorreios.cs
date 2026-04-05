using ProgramacaoOO.Domain;
using ProgramacaoOO.Service;

namespace ProgramacaoOO.Service.Impl;

public class FreteCorreios : ICalculadorFrete
{
    public decimal CalcularFrete(Pedido pedido)
    {
        return 25.00m;
    }
}
