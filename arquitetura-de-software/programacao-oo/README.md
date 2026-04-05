# Sistema de Pedidos em C# (.NET)

## O que o sistema faz

Aplicacao de console para gerenciar pedidos, usuarios e produtos, com suporte a regras de negocio como calculo de frete e processamento de pagamento por meio de estrategias.

## Tecnologias

- C#
- .NET
- Aplicacao Console

## Arquitetura

O projeto esta organizado em camadas simples, separando o dominio das abstracoes de servico:

- `ProgramacaoOO/Domain`: entidades e objetos de dominio (pedido, produto, usuario e status)
- `ProgramacaoOO/Service`: contratos (interfaces) para regras variaveis, como frete e pagamento
- `ProgramacaoOO/Service/Impl`: implementacoes concretas das estrategias de servico
- `ProgramacaoOO/Program.cs`: ponto de entrada da aplicacao

Essa estrutura facilita manutencao, extensao de regras e testes das partes de negocio.

## Como rodar

```bash
dotnet run --project ProgramacaoOO/ProgramacaoOO.csproj
```

## Como gerar build

```bash
dotnet build ProgramacaoOO/ProgramacaoOO.csproj
```
