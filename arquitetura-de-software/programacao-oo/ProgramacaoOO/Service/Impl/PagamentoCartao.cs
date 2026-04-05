using ProgramacaoOO.Domain;
using ProgramacaoOO.Service;

namespace ProgramacaoOO.Service.Impl;

public class PagamentoCartao : IProcessadorPagamento
{
    public bool Processar(Pedido pedido)
    {
        return true;
    }
}
