import textwrap

def menu():
    
    menu = """\n

    ================= MENU =================
    
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo Usuario
    [5]\tNova Conta
    [6]\tListar Contas
    [7]\tSair
    """

    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R${valor:.2f}\n'    
        print('Valor depositado com sucesso!')
    else:
        print('Operação falhou! Digite um valor válido')    

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numeros_saque, limite_saque):
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

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
        print('======== EXTRATO =========')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\n Saldo: R${saldo:.2f}')
        print('==========================')
      

def criar_usuario(usuarios):
    cpf = input('Informe o CPF(somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
         print('Já existe usuário cadastrado com esse CPF!')
         return
    
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Digite a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, nro - bairro, cidade/sigla estado ): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('Usuário cadastrado com sucesso!')


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Conta cadastrada com sucesso!')
        return({'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario})
    
    print('Usuário não encontrado, processo de criação de conta encerrado!')


def listar_contas(contas):
     for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():

    AGENCIA = '0001'
    
    saldo = 0
    limite = 500
    extrato = ""
    numeros_saque = 0
    limite_saque = 3
    usuarios = []
    contas = []


    while True:

        opcao = menu()

        if opcao == "1":
            valor = float(input('Digite o valor do depósito:'))

            saldo, extrato = depositar(saldo, valor, extrato)
             
        elif opcao == "2":
            valor = float(input('Digite o valor do saque:'))
            
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numeros_saque = numeros_saque,
                limite_saque = limite_saque,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                 contas.append(conta)

        elif opcao == "6":
             listar_contas(contas)

        elif opcao == "7":
            break

        else:
            print('Operação inválida, por favor digite novamente a operação desejada')


main()