using ProgramacaoOO.Domain;
using ProgramacaoOO.Service;

namespace ProgramacaoOO.Service.Impl;

public class PagamentoPix : IProcessadorPagamento
{
    public bool Processar(Pedido pedido)
    {
        return true;
    }
}
