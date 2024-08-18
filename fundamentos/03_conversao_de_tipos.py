valor = "10"
variavel_int = int(valor)
variavel_float = float(valor)
variavel_texto = str(variavel_int)

print(variavel_int)
print(variavel_float)
print(variavel_texto)

print(f"A variável [variavel_int] é do tipo {type(variavel_int)} e tem valor {variavel_int}")
print(f"A variável [variavel_float] é do tipo {type(variavel_float)} e tem valor {variavel_float}")
print(f"A variável [variavel_texto] é do tipo {type(variavel_texto)} e tem valor {variavel_texto}")

produto = "Brigadeiro 100% Cacau"
preco = 60.00
print(f"O produto {produto} custa R$ {preco}")