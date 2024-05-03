

def menu():
    menu_str = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo Usuario
    [5] Criar Conta
    [6] Sair

    => """
    return menu_str


def depositar(saldo, valor, extrato):
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    return saldo, extrato



def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
   if valor <= saldo and valor <= limite and numero_saques < limite_saques:
       saldo -= valor
       extrato += f"Saque: R$ {valor:.2f}\n"
       numero_saques += 1
       print("Saque realizado com sucesso!")
   else:
        print("Operação de saque falhou! Verifique seu saldo, limite de saque e número de saques disponíveis.")

   return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuarios(cpf, usuarios):
     usuarios_filtrados = [ usuario for usuario in usuarios if usuario["cpf"] == cpf ]
     return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
     cpf = input("Informe o CPF do usuário: ")
     usuario = filtrar_usuarios(cpf, usuarios)
     
     if usuario:
          print("\n === Conta criada com sucesso! === ")
          return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
     
     print("\n Usuário não encontrado, fluxo de criação de conta encerrado!")


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 10000
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
  


# Laço principal do programa
    while True:
        try:
            opcao = input(menu())

            if opcao == "1": # Operação de depósito
                valor = float(input("Informe o valor que deseja depositar: \n")) # Captura do valor a ser depositado
                if valor > 0:
                 saldo, extrato = depositar(saldo, valor, extrato) # Chamada da função depositar
                else:
                 print("Operação falhou! O valor informado é inválido. Tente Novamente")

            elif opcao == "2": # Operação de saque
                valor_saque = float(input("Informe o valor do saque: "))
                saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor_saque, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

            elif opcao == "3": # Exibir extrato
                exibir_extrato(saldo, extrato=extrato)

            elif opcao == "4": # Novo Usuário
               criar_usuario(usuarios)

            elif opcao == "5": # Criar Conta
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta,usuarios)

                if conta:
                    contas.append(conta)
            
            elif opcao == "6": # Sair
                print("Saindo do programa...")
                break
        
            else:
                print("Opção inválida! Por favor, escolha uma opção válida.")

        except ValueError:
            print("Entrada inválida! Por favor, insira um valor numérico válido.")

main()