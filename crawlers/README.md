# Desafio 2: Crawlers

Essa aplicação tem como função raspar dados do Reddit, listar as threads que tem mais de 5000 Upvotes e
retornar essa lista de threads em um Bot no Telegram a partir de um comando seguido de uma thread (ou lista
de threads) separadas por ponto e vírgula.

## Rodando a aplicação via Docker:

### Passo 1:

Para rodar essa aplicação você deve criar um arquivo .env de acordo com o arquivo .env-sample, preenche-lo com o Token do Telegram que foi enviado por e-mail e então rodar o comando:

```sh
docker build -t <nome-da-imagem>
```
E então:
```sh
docker run <nome-da-imagem>
```
### Passo 2:

No Telegram você deve procurar pelo Bot <em>@ID_wall_reddit_bot</em> e utilizar o comando <code>/nadaparafazer</code> seguido pelo nome de uma thread ou lista de threads (separadas por ponto e vírgula) que deseja buscar.

Exemplo:
```
/nadaparafazer dogs;cats;brazil
```

Após alguns segundos o Bot deve enviar a thread ou lista de threads que tenham mais de 5000 Upvotes.

## Rodando a aplicação localmente:

Para rodar a aplicação localmente, basta navegar até a pasta em seu terminal e rodar o arquivo <code>bot_telegram.py</code>.

Exemplo:
```sh
python bot_telegram.py
```

A aplicação ira rodar e você será capaz de fazer a requisição através do comando <code>/nadaparafazer [lista-de-threads] </code> no Bot do Telegram.