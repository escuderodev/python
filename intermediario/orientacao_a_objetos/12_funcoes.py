# passar funções como parâmetros
def dizer_oi(nome: str):
    return f"Oi {nome}"

def incentivar(nome: str):
    return f"Oi {nome}, vamos aprender Python juntos?"

def exibir_mensagem(mensagem: str):
    print(mensagem)

exibir_mensagem(dizer_oi("Eduardo"))
exibir_mensagem(incentivar("Verônica"))

# inner functions
def function_pai():
    print("Executando function_pai()...")

    def function_filho1():
        print("Executando function_filho1()...")

    def function_filho2():
        print("Executando function_filho2()...")

    function_filho1()
    function_filho2()

function_pai()

# utilizando funções como retorno
def calculadora(operacao):
    def somar(a, b):
        return a + b

    def subtrair(a, b):
        return a - b

    def multiplicar(a, b):
        return a * b

    def dividir(a, b):
        return a / b

    if operacao == "+":
        return somar
    elif operacao == "-":
        return subtrair
    elif operacao == "*":
        return multiplicar
    else:
        return dividir

resultado = calculadora("/")(4, 2)
print(resultado)
