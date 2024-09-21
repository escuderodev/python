import functools

def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        print("antes...")
        resultado = funcao(*args, **kwargs)
        print("depois...")
        return resultado
    return envelope

@meu_decorador
def mensagem(nome, idade):
    print(f"Meu nome é {nome} e tenho {idade} anos de idade.")
    return nome.upper()

resultado = mensagem("Eduardo", 40)
print(resultado)
print(mensagem.__name__)