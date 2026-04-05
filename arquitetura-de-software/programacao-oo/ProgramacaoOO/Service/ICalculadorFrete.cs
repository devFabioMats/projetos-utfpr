using ProgramacaoOO.Domain;

namespace ProgramacaoOO.Service;

public interface ICalculadorFrete
{
    decimal CalcularFrete(Pedido pedido);
}
