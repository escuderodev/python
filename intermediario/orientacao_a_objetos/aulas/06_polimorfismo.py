class Conta:
    def __init__(self, numero: str):
        self._numero = numero
        self._saldo = 0.00

    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self):
        return self._saldo
    
    def depositar(self, valor: float):
        self._saldo += valor
    
    def sacar(self, valor: float):
        if self._saldo >= valor:
            self._saldo -= valor
            print(f"Saque no valor de R$ {valor:.2f} realizado com sucesso!")
            print(f"Novo saldo R$: {self._saldo:.2f}")
        else:
            print("Saldo insuficiente!")
            
    def extrato(self):
        print(f"Conta: {self._numero} | Saldo R$ {self._saldo:.2f}")
    
class Conta_Corrente(Conta):
    def __init__(self, numero: str):
        super().__init__(numero)
        self._taxa_saque = 5.00
        
    def sacar(self, valor: float):
        valor_retirado = valor + self._taxa_saque
        if self._saldo >= valor_retirado:
            self._saldo -= valor_retirado
            print(f"Saque no valor de R$ {valor:.2f} + taxa de saque R$ {self._taxa_saque:.2f} realizado com sucesso!")
            print(f"Novo saldo R$: {self._saldo:.2f}")
        else:
            print("Saldo insuficiente!")
            
class Conta_Poupanca(Conta):
    def __init__(self, numero: str):
        super().__init__(numero)
            
conta_corrente = Conta_Corrente("85040-8")
conta_poupanca = Conta_Poupanca("52486-8")
conta_corrente.depositar(1000)
conta_corrente.extrato()
conta_poupanca.depositar(1000)
conta_poupanca.extrato()
conta_corrente.sacar(500)
conta_poupanca.sacar(500)