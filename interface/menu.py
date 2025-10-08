from operations.sum import sum
from operations.subtraction import subtraction
from operations.multiplication import multiplication
from operations.division import division
from operations.potency import potency

def menu():
    print('=== CALCULADORA ===')
    while True:
        print("\nMENU")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Potência")
        print("6 - Sair")

        opcao = input('ESCOLHA SUA OPERAÇÃO: ')

        if opcao == '6':
            print('=== FINALIZANDO CALCULADORA ===')
            break

        try:
            numeros = input('INFORME OS NÚMEROS: ').split()
            numeros = tuple(map(float, numeros))
        except:
            print('ERRO 001! INFORME APENAS NÚMEROS, TENTE NOVAMENTE!')
            continue

        if opcao == '1':
            total = sum(*numeros)
            simbolo = '+'
        elif opcao == '2':
            total = subtraction(*numeros)
            simbolo = '-'
        elif opcao == '3':
            total = multiplication(*numeros)
            simbolo = 'x'
        elif opcao == '4':
            total = division(*numeros)
            simbolo = '÷'
        elif opcao == '5':

        else:
            print('ERRO 002! Opção inválido!')

        print('RESULTADO:', end=' ')
        print(' {} '.format(simbolo).join(map(str, numeros)), f'= {total:.2f}')