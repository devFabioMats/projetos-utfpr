# Aplicação Cliente/Servidor TCP - Python

Projeto desenvolvido para a disciplina de **Sistemas Distribuídos** da UTFPR.

## 📋 Descrição

Aplicação de chat multicliente utilizando sockets TCP em Python. Múltiplos clientes podem se conectar ao servidor e trocar mensagens entre si em tempo real.

## 🚀 Tecnologias

- **Python 3.x**
- **Socket TCP (SOCK_STREAM)**
- Apenas bibliotecas padrão do Python

## 📁 Estrutura do Projeto

```
projeto-cliente-servidor/
├── Server.py               # Servidor TCP
├── Client.py               # Cliente TCP
├── JUSTIFICATIVA_TCP.md    # Documentação técnica
└── README.md              # Este arquivo
```

## 🔧 Como Executar

### 1. Iniciar o Servidor

Em um terminal, execute:

```bash
python Server.py
```

O servidor iniciará na porta **5000** por padrão.

Saída esperada:
```
[INICIANDO] Servidor TCP rodando em 0.0.0.0:5000
[AGUARDANDO] Esperando por conexões...
```

### 2. Conectar Clientes

Em outros terminais (podem ser múltiplos), execute:

```bash
python Client.py
```

O cliente solicitará:
- **IP do servidor** (pressione Enter para usar localhost)
- **Porta** (pressione Enter para usar 5000)
- **Nome de usuário**

### 3. Enviar Mensagens

Após conectar, digite suas mensagens e pressione Enter. As mensagens serão enviadas para todos os outros clientes conectados.

Para sair, digite: `sair`

## 💡 Exemplo de Uso

### Terminal 1 - Servidor
```
Servidor iniciado na porta 50250
Lista de sockets: [<socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('0.0.0.0', 50250)>]
Cliente conectado de ('127.0.0.1', 52341)
Cliente conectado de ('127.0.0.1', 52342)
Mensagem recebida de ('127.0.0.1', 52341): João: Oi pessoal!
Enviando para ('127.0.0.1', 52342)
```

### Terminal 2 - Cliente 1 (João)
```
Iniciando cliente
Digite o IP do servidor 
>>127.0.0.1
Digite a porta do servidor
>>50250
Conectando...
Conectado!
Digite seu nome de usuário
>>João
Iniciando serviço de recebimento
>>Oi pessoal!
>>
```

### Terminal 3 - Cliente 2 (Maria)
```
Iniciando cliente
Digite o IP do servidor 
>>127.0.0.1
Digite a porta do servidor
>>50250
Conectando...
Conectado!
Digite seu nome de usuário
>>Maria
Iniciando serviço de recebimento
João: Oi pessoal!
>>Oi João, tudo bem?
>>
```

## 🔍 Características Técnicas

### Protocolo TCP

- ✅ **Confiável:** Garante entrega de todas as mensagens
- ✅ **Ordenado:** Mensagens chegam na ordem enviada
- ✅ **Controle de Fluxo:** Evita sobrecarga
- ✅ **Detecção de Erros:** Checksums automáticos

### Arquitetura

- **Servidor Multicliente:** Aceita múltiplas conexões simultâneas
- **Threading:** Gerencia clientes em threads separadas  
- **Broadcast:** Mensagens são retransmitidas entre clientes
- **Select:** Monitora múltiplos sockets simultaneamente
- **Baseado no projeto de Segurança:** Estrutura similar, sem criptografia

## 📚 Documentação

Para entender as **razões técnicas** do uso do protocolo TCP, consulte:

👉 [JUSTIFICATIVA_TCP.md](./JUSTIFICATIVA_TCP.md)

Este documento contém:
- Comparação TCP vs UDP
- Justificativas detalhadas
- Análise de casos de uso
- Diagramas e exemplos

## 🛠️ Requisitos

- Python 3.6 ou superior
- Bibliotecas padrão (socket, threading, sys)

Não requer instalação de pacotes externos!

## 📝 Observações

1. **Múltiplos clientes:** O servidor aceita várias conexões simultâneas
2. **Porta 50250:** Mesma porta do projeto de segurança
3. **Comandos:** Digite `exit` para sair do cliente
4. **Threading:** Usa select() para gerenciar múltiplos sockets
5. **Broadcast:** Mensagens são enviadas para todos os outros clientes conectados

## 🎓 Atividade Acadêmica

Este projeto atende aos requisitos da tarefa:
- ✅ Aplicação cliente/servidor em Python
- ✅ Protocolo da camada de aplicação (troca de strings)
- ✅ Uso do protocolo TCP
- ✅ Justificativa detalhada do uso do TCP
- ✅ Código limpo e comentado

## 👨‍💻 Autor

**UTFPR - Universidade Tecnológica Federal do Paraná**  
Disciplina: Sistemas Distribuídos  
Ano: 2025
