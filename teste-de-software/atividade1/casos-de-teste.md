# Casos de Teste - atividade1.js

## CT-001
- id: CT-001
- descricao: Retorna o indice do ultimo zero quando ha mais de um zero no vetor.
- entrada(s): [4, 2, 0, 7, 0, 9]
- saida(s): 4
- procedimento de execucao:
  1. Abrir terminal na pasta do projeto.
  2. Executar o arquivo JavaScript com `node atividade1.js`.
  3. Verificar o valor exibido no console.
- pre-condicoes:
  - Node.js instalado.
  - Arquivo `atividade1.js` presente na pasta do projeto.

## CT-002
- id: CT-002
- descricao: Retorna -1 quando o vetor nao contem zero.
- entrada(s): [1, 2, 3, 4]
- saida(s): -1
- procedimento de execucao:
  1. Alterar temporariamente `vectorExample` para [1, 2, 3, 4, 5, 6] no arquivo `atividade1.js`.
  2. Executar `node atividade1.js`.
  3. Confirmar se o console mostra -1.
- pre-condicoes:
  - Node.js instalado.
  - Permissao para editar e executar `atividade1.js`.

## CT-003
- id: CT-003
- descricao: Retorna 0 quando o unico zero esta na primeira posicao.
- entrada(s): [0, 5, 8]
- saida(s): 0
- procedimento de execucao:
  1. Alterar temporariamente `vectorExample` para [0, 5, 8] em `atividade1.js`.
  2. Executar `node atividade1.js`.
  3. Validar se o resultado no console e 0.
- pre-condicoes:
  - Node.js instalado.
  - Arquivo `atividade1.js` sem erros de sintaxe.

## CT-004
- id: CT-004
- descricao: Retorna o ultimo indice quando todos os elementos sao zero.
- entrada(s): [0, 0, 0, 0]
- saida(s): 3
- procedimento de execucao:
  1. Alterar temporariamente `vectorExample` para [0, 0, 0, 0, 0, 0] em `atividade1.js`.
  2. Executar `node atividade1.js`.
  3. Confirmar se o valor retornado e 3.
- pre-condicoes:
  - Node.js instalado.
  - Comando `node atividade1.js` funcional no terminal.