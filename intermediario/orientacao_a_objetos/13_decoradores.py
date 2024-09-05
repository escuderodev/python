def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes da função passada como parâmetro.")
        funcao()
        print("Faz algo depois da função passada como parâmetro.")
    return envelope

def ola_mundo():
    print("Olá mundo!")

ola_mundo = meu_decorador(ola_mundo)
ola_mundo()