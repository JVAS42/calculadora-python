from operations.sum import sum
from operations.subtraction import subtraction
from operations.multiplication import multiplication
from operations.division import division

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

        if opcao == '1':
            try:
                numeros = input('INFORME OS NÚMEROS: ').split()
                numeros = tuple(map(float, numeros))
                total = sum(*numeros)
                print('A SOMA TOTAL', end=' ⭢ ')
                for i in range(len(numeros)):
                    if i == (len(numeros) - 1):
                        print(f'{numeros[i]:.2f} = {total:.2f}')
                    else:
                        print(f'{numeros[i]}', end=' + ')
            except:
                print('ERRO 001. INFORME APENAS NÚMEROS, TENTE NOVAMENTE!')

        elif opcao == '2':
            try:
                numeros = input('INFORME OS NÚMEROS: ').split()
                numeros = tuple(map(float, numeros))
                total = subtraction(*numeros)
                print('A SUBTRAÇÃO TOTAL', end=' ⭢ ')
                for i in range(len(numeros)):
                    if i == (len(numeros) - 1):
                        print(f'{numeros[i]:.2f} = {total:.2f}')
                    else:
                        print(f'{numeros[i]}', end=' - ')
            except:
                print('ERRO 001. INFORME APENAS NÚMEROS, TENTE NOVAMENTE!')
        
        elif opcao == '3':
            try:
                numeros = input('INFORME OS NÚMEROS: ').split()
                numeros = tuple(map(float, numeros))
                total = multiplication(*numeros)
                print('A SUBTRAÇÃO TOTAL', end=' ⭢ ')
                for i in range(len(numeros)):
                    if i == (len(numeros) - 1):
                        print(f'{numeros[i]:.2f} = {total:.2f}')
                    else:
                        print(f'{numeros[i]}', end=' x ')
            except:
                print('ERRO 001. INFORME APENAS NÚMEROS, TENTE NOVAMENTE!')
        
        elif opcao == '4':
            try:
                numeros = input('INFORME OS NÚMEROS: ').split()
                numeros = tuple(map(float, numeros))
                total = division(*numeros)
                print('A SUBTRAÇÃO TOTAL', end=' ⭢ ')
                for i in range(len(numeros)):
                    if i == (len(numeros) - 1):
                        print(f'{numeros[i]:.2f} = {total:.2f}')
                    else:
                        print(f'{numeros[i]}', end=' ÷ ')
            except:
                print('ERRO 001. INFORME APENAS NÚMEROS, TENTE NOVAMENTE!')
        
        elif opcao == '5':
            print('POTENCIA')
        elif opcao == '6':
            print('=== CALCULADORA ENCERRADA ===')
            break