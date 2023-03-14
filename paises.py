import json
import sys

import requests


URL_TODOS_PAISES = "https://restcountries.com/v3.1/all"
URL_PAIS = "https://restcountries.com/v3.1/name/"


# faz a requisição e depois realiza o parsing do texto obtido de string para json
def carregar_paises():
    try:
        resposta_todos_paises = requests.get(URL_TODOS_PAISES)
        lista_paises = json.loads(resposta_todos_paises.text)

        return lista_paises
    except Exception as error:
        print('Erro ao carregar os países no endpoint: {}'.format(URL_TODOS_PAISES))
        print('Erro: {}'.format(error))


# faz a requisição e depois realiza o parsing do texto obtido de string para json
def informar_pais(pais):
    try:
        resposta_pais = requests.get(URL_PAIS + pais)
        lista_pais = json.loads(resposta_pais.text)

        return lista_pais
    except Exception as error:
        print('Erro ao carregar os país no endpoint: {}'.format(URL_PAIS + pais))
        print('Erro: {}'.format(error))


def retornar_nomes(lista):
    nomesPaises = []
    for pais in lista:
        for chave, valor in pais.items():
            if (chave == 'name'):
                for chaveNome, valorNome in valor.items():
                    if (chaveNome == 'official'):
                        nomesPaises.append(valorNome)
    return sorted(nomesPaises)


def retornar_moedas(lista):
    nomesMoedas = []
    for pais in lista:
        for chave, valor in pais.items():
            if (chave == 'currencies'):
                for valorAbreviatura in valor.values():
                    for chaveNomeMoeda, valorNomeMoeda in valorAbreviatura.items():
                        if (chaveNomeMoeda == 'name'):
                            nomesMoedas.append(valorNomeMoeda)
    return sorted(nomesMoedas)


def retornar_capitais(lista):
    nomesCapitais = []
    for pais in lista:
        for chave, valor in pais.items():
            if (chave == 'capital'):
                nomesCapitais.append(valor)
    return sorted(nomesCapitais)


def retornar_linguagens(lista):
    linguagensOficiais = []
    for pais in lista:
        for chave, valor in pais.items():
            if (chave == 'languages'):
                for valorNomeLinguagem in valor.values():
                    linguagensOficiais.append(valorNomeLinguagem)
    linguagensOficiais = retirar_repetidos_lista(linguagensOficiais)
    return sorted(linguagensOficiais)


def retirar_repetidos_lista(lista):
    listaSemRepeticao = []
    for elemento in lista:
        if (elemento not in listaSemRepeticao):
            listaSemRepeticao.append(elemento)
    return listaSemRepeticao


if __name__ == '__main__':
    print('Bem vindo às informações de 250 países disponíveis no site `restcountries`\n')

    if (len(sys.argv) > 1):
        pais = sys.argv[1]

        sobrePaisEspecifico = informar_pais(pais)
        print(retornar_nomes(sobrePaisEspecifico))
        print(retornar_capitais(sobrePaisEspecifico))
        print(retornar_linguagens(sobrePaisEspecifico))
        print(retornar_moedas(sobrePaisEspecifico))
    else:
        print('Se desejar saber de um país específico, chame o programa como o exemplo a seguir -> `python paises.py brazil`')
        paises = carregar_paises()
        print(retornar_nomes(paises))
        print(retornar_capitais(paises))
        print(retornar_linguagens(paises))
        print(retornar_moedas(paises))
