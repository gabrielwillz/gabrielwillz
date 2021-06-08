import pandas as pd
import numpy as np
import json
import time
from datetime import date
import requests
from bs4 import BeautifulSoup

print('######################################')
print('########## Web Scraping OLX ##########')
print('######################################')
print()
print('------------------------------------------------------------------------------------------------')
print(
    'Opcoes de dados: \n #pages = quantidade de paginas \n #regiao = SP, RJ \n #busca = 1 para IPhone | 2 para carro | 3 para notebook | 4 para computador')

Lista_Final = []

pag = int(input('Quantas Paginas quer extrair? INSIRA ---> '))
reg = str(input('Qual regiao voce quer? INSIRA ---> '))
bus = str(input('Qual numero da busca? INSIRA ---> '))


def BuscarDadosOLX(pages=2, regiao='SP', busca='1'):
    RegiaoBuscar = {'SP': 'sao-paulo-e-regiao', 'RJ': 'rio-de-janeiro-e-regiao'}
    Prefix = {'SP': 'sp', 'RJ': 'rj'}
    ObjetoBusca = {'1': 'iphone', '2': 'carro', '3': 'notebook', '4': 'computador'}
    for x in range(0, pages):
        # print('Loop NUMERO: ' + str(x))
        url = 'https://' + Prefix[regiao] + '.olx.com.br/' + RegiaoBuscar[regiao] + '?q=' + ObjetoBusca[busca]
        if x == '0':
            print('somente a primeira pagina')
        else:
            url = 'https://' + Prefix[regiao] + '.olx.com.br/' + RegiaoBuscar[regiao] + '?o=' + str(x) + '&q=' + \
                  ObjetoBusca[busca]
            # print(url)

    PARAMS = {
        'authority': 'sp.olx.com.br',
        'method': 'GET',
        'scheme': 'https',
        'referer': 'https://sp.olx.com.br/sao-paulo-e-regiao?q=iphone',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
    }

    page = requests.get(url=url, headers=PARAMS)
    soup = BeautifulSoup(page.content, 'lxml')
    itens = soup.find_all("li", {"class": "sc-1fcmfeb-2 juiJqh"})

    for a in itens:
        try:
            nomeItem = a.findAll('h2', class_="sc-1iuc9a2-1 daMDOK sc-ifAKCX eKQLlb")[0].contents[0]
            precoItem = a.findAll('p', class_='sc-ifAKCX eoKYee')[0].contents[0]
            precoItem = precoItem.split('R$')[1]
            precoItem = float(precoItem.replace('.', ''))
            diaPostagem = a.findAll('p', class_='sc-1iuc9a2-4 hDBjae sc-ifAKCX fWUyFm')[0].contents[0]
            urlItem = a.find('a')['href']

            json = {
                'DIA DA POSTAGEM': diaPostagem,
                'NOME DO ITEM': nomeItem,
                'PRECO DO ITEM': precoItem,
                'URL DO ANUNCIO': urlItem
            }

            Lista_Final.append(json)
        except:
            print('erro')

    print('ARQUIVO PRONTO! :))')


BuscarDadosOLX(pages=pag, regiao=reg, busca=bus)
df = pd.DataFrame(Lista_Final)
df.to_excel('Lista_Final.xlsx')