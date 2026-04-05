using ProgramacaoOO.Domain;

namespace ProgramacaoOO.Service;

public interface IProcessadorPagamento
{
    bool Processar(Pedido pedido);
}
