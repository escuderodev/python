def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes da função passada como parâmetro.")
        funcao()
        print("Faz algo depois da função passada como parâmetro.")
    return envelope

# # definindo a função ola_mundo e utilizando decorador de forma raiz
# def ola_mundo():
#     print("Olá mundo!")

# ola_mundo = meu_decorador(ola_mundo)
# ola_mundo()

# definindo a função ola_mundo e utilizando decorador de forma simplificada
@meu_decorador
def ola_mundo():
    print("Olá mundo!")
    
ola_mundo()