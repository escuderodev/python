class Conta:
    def __init__(self, numero: str, cliente: str):
        self._agencia = "0001"
        self._numero = numero
        self._saldo = 0.00
        self._cliente = cliente
        
    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque no valor de R$ {valor:.2f} realizado com sucesso!")
            print(f"Novo saldo R$: {self._saldo:.2f}")
        else:
            print("Saldo insuficiente!")
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito no valor de R$ {valor:.2f} realizado com sucesso!")
            print(f"Novo saldo R$: {self._saldo:.2f}")
            
    def extrato(self):
        print(f"""
    ======== Extrato ========
    Ag.: {self._agencia}
    Conta: {self._numero}
    Cliente: {self._cliente}
    Saldo: {self._saldo:.2f}
    """)
    
conta = Conta("85040-5", "Eduardo Escudero")
conta.extrato()
conta.depositar(1000)
conta.extrato()
conta.sacar(999)
conta.extrato()