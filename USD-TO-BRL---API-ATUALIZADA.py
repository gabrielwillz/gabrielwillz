import requests
import json
import time


def main():
    def titulo():
        print('''                   #########################
                   ####### USD TO BRL ###### 
                   #########################
                ''')

    def api():
        contacao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
        contacao = contacao.json()
        contacao_dolar = contacao['USDBRL']['bid']
        return float(contacao_dolar)

    def calculo(a, b):
        print(f'Valor final: ', a * b)

    def modelo():
        cont = api()
        print()
        print('----------------------------------------------')
        print()
        print(f'CONTAÇAO ATUAL DO DOLAR: {cont} |||| VALOR INSERIDO: {valor_inserido}')
        print()
        print('----------------------------------------------')
        print()

    titulo()
    print()
    valor_inserido = float(input('QUANTOS VOCE QUER CONVERTER?: '))
    modelo()
    calculo(valor_inserido, api())
    print()

    option = int(input('Quer fazer outro calculo?\n 1. SIM\n 2. NÃO\n'))

    if option == 1:
        main()
    else:
        print('Saindo.......')


main()
if __name__ == '__main__':
    main()