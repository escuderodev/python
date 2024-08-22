saldo = 0
limite_por_saque = 500.00
soma_dos_saques_realizados_no_dia = 0
LIMITE_DE_SAQUES_POR_DIA = 3
extrato = []

def depositar(valor):
    global saldo
    saldo += valor
    extrato.append(f"+ R$ {valor:.2f}")
    print(f"Depósito no valor de R$ {valor:.2f} realizado com sucesso!")
    print(f"Saldo atual R$ {saldo:.2f}")
    
def sacar(valor):
    global saldo
    global limite_por_saque
    global soma_dos_saques_realizados_no_dia
    global extrato
    global LIMITE_DE_SAQUES_POR_DIA
    if valor > limite_por_saque:
        print(f"O valor R$ {valor:.2f} excede o limite permitido por saque. Saque não realizado!")
    elif LIMITE_DE_SAQUES_POR_DIA == 0:
        print("Você já atingiu o limite de saques diários que é 3. Saque não realizado!")
    elif soma_dos_saques_realizados_no_dia > 1000.00:
        print("O valor solicitado excede o limite diário permitido para saques. Saque não realizado!")
    elif valor <= saldo:
        saldo -= valor
        soma_dos_saques_realizados_no_dia += valor
        LIMITE_DE_SAQUES_POR_DIA -= 1
        extrato.append(f"- R$ {valor:.2f}")
        print(f"Saque no valor de R$ {valor:.2f} realizado com sucesso!")
        print(f"Saldo atual R$ {saldo:.2f}")
    else:
        print(f"Saldo insuficiente!")

def gera_extrato():
    global extrato
    for transacao in extrato:
        print(f"{transacao}")
    print(f"Saldo atual R$: {saldo:.2f}")
    
def exibir_menu():
    print("\n=== Bem vindo ao DioBank ===")
    
    while True:
        opcao = input("\nDigite D para Depósito, S para Saque, E para Extrato ou Q para Sair: ")
        
        if opcao.upper() == "D":
            valor = float(input("Digite o valor do depósito R$: "))
            depositar(valor)
        elif opcao.upper() == "S":
            valor = float(input("Digite o valor do saque R$: "))
            sacar(valor)
        elif opcao.upper() == "E":
            gera_extrato()
        elif opcao.upper() == "Q":
            print("Encerrando o sistema!")
            break
        else:
            print("Opção inválida!")
            
exibir_menu()