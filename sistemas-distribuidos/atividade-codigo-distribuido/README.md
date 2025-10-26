# Multiplicação Distribuída de Matrizes - TCP

## Como executar o sistema

### 1. Preparar o ambiente
- Certifique-se que tem Python instalado
- Todos os arquivos devem estar na mesma pasta

### 2. Iniciar o servidor
```
python matriz_server.py
```

- Digite o tamanho da matriz quando solicitado (ex: 3, 4, 5...)
- O sistema vai gerar matrizes aleatórias
- Vai calcular tempo sequencial e paralelo automaticamente
- Digite quantos workers você quer usar (ex: 2, 3, 4...)
- Aguarde os workers se conectarem

### 3. Iniciar os workers (clientes)
Para cada worker, abra um terminal novo e execute:
```
python matriz_client.py
```

- Aperte Enter quando pedir o IP (usa localhost por padrão)
- O worker vai processar automaticamente e desconectar

### 4. Exemplo completo

**Terminal 1 (Servidor):**
```
python matriz_server.py
Digite o tamanho da matriz: 4
Quantos workers voce quer usar? 2
```

**Terminal 2 (Worker 1):**
```
python matriz_client.py
Digite o IP do servidor (ou enter para localhost): [ENTER]
```

**Terminal 3 (Worker 2):**
```
python matriz_client.py
Digite o IP do servidor (ou enter para localhost): [ENTER]
```

### 5. Resultado
- O servidor mostra os tempos de execução
- Arquivo `tempoAlgoritmos.txt` é criado automaticamente
- Contém comparação dos três métodos: sequencial, paralelo e distribuído

### Observações
- Inicie PRIMEIRO o servidor
- Depois inicie os workers na quantidade que você especificou
- O sistema divide o trabalho igualmente entre os workers
- Matrizes maiores mostram melhor a diferença de performance