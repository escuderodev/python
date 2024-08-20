print("\n=== Testando a função exibir_mensagem() ===")
def exibir_mensagem(mensagem):
    print(f"\n=== {mensagem} ===")
    
def soma(num1, num2):
    exibir_mensagem("Testando a função soma()")
    print(f"{num1} + {num2} = {num1 + num2}")
    
def tabuada(multiplicador):
    exibir_mensagem("Testando a função tabuada()")
    for contador in range(0, 11):
        print(f"{multiplicador} x {contador} = {multiplicador * contador}")
        
def sacar(valor):
    exibir_mensagem("Testando a função sacar()")
    saldo = 1000
    if(saldo >= valor):
        saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        print(f"Seu novo saldo é R$: {saldo:.2f}.")

def retorna_antecessor_e_sucessor(numero):
    exibir_mensagem("Testando a função retorna_antecessor_e_sucessor()")
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor
        
exibir_mensagem("Palmeiras não tem mundial!")
soma(10, 5)
tabuada(7)
sacar(498)
print(retorna_antecessor_e_sucessor(5))