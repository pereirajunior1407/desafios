# Desafio 1: Strings

Após ler o coding style do kernel Linux, você descobre a mágica que é
ter linhas de código com no máximo 80 caracteres cada uma.

Assim, você decide que de hoje em diante seus e-mails enviados também
seguirão um padrão parecido e resolve desenvolver um plugin para te ajudar
com isso. Contudo, seu plugin aceitará no máximo 40 caracteres por linha.

A aplicação a seguir recebe:
1. um texto qualquer
2. um limite de comprimento

A partir disso, a aplicação é capaz de formatar o texto a fim de que haja
uma quebra de linha sempre que alcançar o limite de caractéres estabelecido.

## Rodando a aplicação

Assumindo que o Python esteja instalado corretamente e no Path, para executar
a aplicação você deve usar o seguinte comando:

```sh
python app.py
```

A seguir você deve inserir o texto que deseja formatar e o limite de caractéres
por linha.

## Exemplo de input

`In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.`

`And God said, "Let there be light," and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light "day," and the darkness he called "night." And there was evening, and there was morning - the first day.`

## Testes unitários:

Essa resolução do desafio proposto conta com testes unitários.
Os testes tem o propósito de:

- Conferir se o campo de texto foi preenchido;
- Conferir se o campo de limite de caractéres foi preenchido;
- Conferir se o campo de limite de caractéres é igual á Zero;
- Conferir se o campo de limite de caractéres é negativo;

Para rodar os testes da aplicação, você deve usar o seguinte comando:

```sh
python test_text_formatter.py
```

A resposta deve aparecer da seguinte forma:

```sh
...
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```
