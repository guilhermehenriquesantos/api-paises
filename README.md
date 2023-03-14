# API - PAÍSES

## Tipos de entrada

- `python paises.py`
- `python paises.py brazil`

## Funções realizadas

- **Carregar os países:** realiza a requisição de todos os países na URL da API, recebe um texto e realiza o *parsing* (transformar texto obtido em JSON)
- **Informar sobre um país:** realiza a requisição do país escolhido na URL da API, recebe um texto e realiza o *parsing* (transformar texto obtido em JSON)
- **Retornos de informações:** nomes, moedas, capitais e línguas oficiais

## Comandos utilizados na construção

- **Para criar um ambiente `virtualenv:`** `--always-copy` permite que seja criado em um partição montada, por exemplo, um HD.
  - **`virtualenv ambiente_desenvolvimento_api_paises_pyVersion --always-copy`**

## Conceitos importantes

- **Virtualenv:** ambiente de desenvolvimento python criado especificamente para um projeto, pois com esse benefício, caso ocorra atualizações na linguagem python por exemplo, o ambiente virtual escolhido sempre será o mesmo, dessa forma, em futuras manutenções será usado o ambiente correto, evitando que determinadas funcionalidades deixem de funcionar com o upgrade da linguagem, pois a linguagem utilizada será sempre a do virtualenv.
- **Parsing:** pegar um texto e transformar na entrada que deseja, **TEXTO -> JSON | TEXTO -> HTML | TEXTO -> XML**, etc.