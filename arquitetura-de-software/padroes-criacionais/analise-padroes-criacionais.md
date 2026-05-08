# Padrões Criacionais - Entendimento, Exemplos e Análise

## Factory Method
Para mim, o Factory Method resolve o problema de criar objetos sem amarrar o código cliente a classes concretas. Em vez de usar `new` diretamente em vários lugares, eu concentro a decisão de criação em fábricas específicas.

**Exemplo de aplicação:** em um sistema de pedidos, posso enviar notificações por e-mail ou SMS. O cliente usa uma fábrica de notificador e não precisa saber qual classe concreta está sendo criada.

## Abstract Factory
Eu entendo o Abstract Factory como uma evolução do Factory Method para criar famílias de objetos relacionados. Ele garante que os objetos criados sejam compatíveis entre si.

**Exemplo de aplicação:** em uma interface multiplataforma, uma fábrica cria componentes para Web (botão e input Web) e outra para Mobile (botão e input Mobile). O cliente monta a tela sem se preocupar com detalhes de implementação.

## Builder
O Builder é útil quando o objeto final possui muitos campos ou combinações. Em vez de um construtor gigante, eu monto o objeto passo a passo, de forma mais legível e segura.

**Exemplo de aplicação:** montagem de um objeto `Computer` com CPU, RAM, armazenamento e GPU opcional. Assim fica fácil criar versões diferentes, como máquina de escritório e máquina gamer.

## Prototype
Para mim, o Prototype serve para criar novos objetos copiando um objeto já existente. Isso economiza esforço quando existe uma configuração base que se repete.

**Exemplo de aplicação:** criação de currículos a partir de um modelo base. Eu clono o template e altero apenas nome e habilidades de cada pessoa.

## Singleton
O Singleton garante que apenas uma instância exista durante toda a execução do sistema, com um ponto global de acesso.

**Exemplo de aplicação:** configurações globais da aplicação (tema, idioma, ambiente). Qualquer parte do sistema acessa a mesma instância e enxerga os mesmos valores.

## Padrão mais interessante (análise subjetiva)
O padrão que considero mais interessante é o **Builder**. Na prática, ele melhora bastante a clareza do código em objetos complexos, reduz a chance de erro em parâmetros e facilita evolução futura. Também é simples de explicar e de aplicar no dia a dia, principalmente em sistemas que montam entidades com muitos dados opcionais.
