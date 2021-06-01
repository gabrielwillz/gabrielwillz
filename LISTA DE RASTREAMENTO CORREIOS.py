import requests
from bs4 import BeautifulSoup

def main():
    print('###############################')
    print('#### LISTA DE RASTREAMENTO ###')
    print('###############################')
    print()

    codigos = int(input('Quantos rastreamentos quer fazer?: '))
    lista_rastreo = []

    i = 1
    while i <= codigos:
        codigo_rastreo = str(input('Coloque o numero de rastreio: '))
        lista_rastreo.append(codigo_rastreo)
        i += 1

    print('-------------------------------------')
    print()
    print(f'Numero de Codigos de RASTREAMENTOS: {codigos}')
    print()
    print('####### LISTA DE RASTREAMENTO ###########')
    print()

    for codigo in lista_rastreo:
        req = requests.post(url='https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm?',
                            data={'objetos': codigo})
        soup = BeautifulSoup(req.text, 'html.parser')
        ult_atu = soup.find(id="UltimoEvento").strong.text
        data = soup.find(id="UltimoEvento").text.split()[-1]
        print(f'Status: {ult_atu} - Data: {data} - CODIGO: {codigo}')
        print()
        print('-------------------------------------------------------------')
        print()

    option = int(input('Quer fazer outra lista de Rastreamento?\n 1. SIM\n 2. NÃO\n'))

    if option == 1:
        main()
    else:
        print('Saindo.......')


if __name__ == '__main__':
    main()
