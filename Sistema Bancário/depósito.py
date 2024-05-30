cliente = str(input('Digite seu nome por favor:'))

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

    """

saldo = 0
limite = 500
extrato = ""
numeros_saque = 0
limite_saque = 3


while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input('Digite o valor do depósito:'))
    
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R${valor:.2f}\n'
    
        else:
            print('Operação falhou! Digite um valor válido')    



    elif opcao == "2":
        valor = float(input('Digite o valor do saque:'))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numeros_saque >= limite_saque

        if excedeu_saldo:
            print('Operação falhou! Saldo indisponível')

        elif excedeu_limite:
            print('Operação falhou! Você já excedeu o limite diário de saque disponível')

        elif excedeu_saque:
            print('Operação falhou! Você já excedeu a quantidade de saques diários disponíveis')

        elif valor > 0:
            saldo -= valor
            extrato += (f'Saque: R${valor:.2f}\n')
            numeros_saque += 1

        else:
            print('Operação falhou! O valor informado é inválido.')



    elif opcao == "3":
        print('======== EXTRATO =========')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\n Saldo: R${saldo:.2f}')
        print('==========================')



    elif opcao == "4":
        break

    else:
        print('Operação inválida, por favor digite novamente a operação desejada')