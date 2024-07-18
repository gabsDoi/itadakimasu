# Itadakimasu - Um protótipo de app de Delivery (pt-br)

Este código foi desenvolvido como projeto principal do curso ***Python: crie sua primeira aplicação*** da escola de programação [Alura](https://www.alura.com.br/).

### Estrutura
O projeto ele tem a estrutura base para um app de Delivery, como o Ifood.
Nele, foram utilizados códigos como:
  - Estrutura `if` e `else`
  - Loops com `for`
  - `try` e `except`
  - Código ternário
  - Variáveis, Listas e Dicionários

### Funcionalidade
O projeto é rodado no terminal da IDE do usuário, e sua interface inicial é dessa forma:
```
- - - Itadakimasu - - -

1. Cadastrar restaurante
2. Listar restaurantes
3. Ativar restaurante
4. Sair

Escolha uma opção:
```
O projeto tem uma interface bem simples para o usuário.
No campo "Escolha uma opção" o usuário pode digitar algum dos números das opções acima e assim executá-las. Caso o usuário digitar um número que não seja das opções ou mesmo digitar uma letra, o sistema irá identificar um erro, dando uma mensagem de invalidação e voltando para a tela inicial:
```
Opção inválida! Digite novamente


- - - Itadakimasu - - -

1. Cadastrar restaurante
2. Listar restaurantes
3. Ativar restaurante
4. Sair

Escolha uma opção:
```
Ele apresenta as opções de:
  1. Cadastrar restaurante
     - Pergunta o nome do restaurante e qual o tipo do restaurante que deseja cadastrar
     - Caso der algum erro, ele acionará uma mensagem e voltará para a tela principal
  2. Listar restaurantes
     - Lista os restaurantes cadastrados, mostrando em cada linha um restaurante, com seu respectivo nome, tipo e status
     - Caso não houver restaurantes, é exibido uma mensagem de nenhum restaurante cadastrado
  3. Ativar restaurante
     - Faz uma busca do nome do restaurante, e caso o restaurante estiver cadastrado, ele irá alterar seu status (de desativado para ativado e vice versa)
     - Caso o nome do restaurante não for idêntico ao cadastrado, exibirá uma mensagem de que não foi possível encontrar o restaurante
  4. Sair
     - Finaliza o programa, limpando toda a tela inicial
  
### Considerações finais
Fiz algumas pequenas mudanças em relação ao projeto original do curso
  - Criei um nome próprio (Itadakimasu)
  - Utilizei a biblioteca `time`
  - Adicionei algumas funcionalidades

Este foi meu primeiro projeto em _Python_!

Espero que tenha gostado :smile:
