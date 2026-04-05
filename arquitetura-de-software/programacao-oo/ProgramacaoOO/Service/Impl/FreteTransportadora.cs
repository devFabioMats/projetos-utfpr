using ProgramacaoOO.Domain;
using ProgramacaoOO.Service;

namespace ProgramacaoOO.Service.Impl;

public class FreteTransportadora : ICalculadorFrete
{
    public decimal CalcularFrete(Pedido pedido)
    {
        return 35.00m;
    }
}
