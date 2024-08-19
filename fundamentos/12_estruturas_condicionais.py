# === if padrão ===
print("\n=== if padrão ===")
idade = 17
acompanhado = True

if(idade >= 18):
    print(f"Você tem {idade} anos e é maior de idade!")
elif(idade < 18 and acompanhado):
    print(f"Você tem {idade} anos, é menor de idade, mas está acompanhado!")
else:
    print(f"Você tem {idade} anos, é menor de idade e está desacompanhado!")
    
# === if aninhado ===
print("\n=== if aninhado ===")
movimentacao_publicavel = False
possui_advogado_marcado = True
possui_reu_revel_marcado = False

if(movimentacao_publicavel):
    if(possui_advogado_marcado):
        print("Movimentação Publicável e possui Advogado marcado => Publica!")
    elif(possui_reu_revel_marcado):
        print("Movimentação Publicável e possui Réu Revel marcado => Publica!")
    else:
        print("Movimentação Publicável, mas não possui Advogado ou Réu Revel marcado => Não Publica!")
else:
    print("Movimentação não publicável!")

# === if ternário ===
print("\n=== if ternário ===")
saldo = 1000
saque = 1500
status = "Saque realizado com sucesso!" if saldo >= saque else "Saldo Insuficiente!"
print(status)
        