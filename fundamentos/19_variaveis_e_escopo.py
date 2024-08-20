nome = "Eduardo" # variável global
ano_nascimento = 1984 # variável global

def exibir_mensagem():
    global nome
    global ano_nascimento
    ano_atual = 2024 # variável local
    idade = ano_atual - ano_nascimento
    print(f"Meu nome é {nome} e tenho {idade} anos de idade.")
    
exibir_mensagem()