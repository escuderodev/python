saldo = 0
limite_por_saque = 500.00
soma_dos_saques_realizados_no_dia = 0
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
    if valor > limite_por_saque:
        print(f"O valor R$ {valor:.2f} excede o limite permitido por saque!")
    elif soma_dos_saques_realizados_no_dia > 1000.00:
        print("O valor solicitado excede o limite diário permitido para saques. Saque não realizado!")
    elif valor <= saldo:
        saldo -= valor
        soma_dos_saques_realizados_no_dia += valor
        extrato.append(f"- R$ {valor:.2f}")
        print(f"Saque no valor de R$ {valor:.2f} realizado com sucesso!")
    else:
        print(f"Saldo insuficiente!")

def gera_extrato():
    global extrato
    for transacao in extrato:
        print(f"{transacao}")
    print(f"Saldo atual R$: {saldo:.2f}")
        

print("\n=== Depositando Valor ===")
depositar(2000.00)

print("\n=== Sacando Valor ===")
sacar(500.00)
sacar(501.00)
sacar(500.00)
sacar(500.00)
sacar(1.00)

print("\n=== Gerando Extrato ===")
gera_extrato()