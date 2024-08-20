# === for clássico ===
print("\n=== for clássico ===")
texto = input("Informe um texto qualquer: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra.upper(), end = " ")

print() #pula uma linha

# === função range ===
print("\n=== função range ===")
print(list(range(4)))
print(list(range(0,11)))

# === for clássico + range() ===
print("\n=== tabuada com for clássico + range() ===")
multiplicador = 2

for contador in range(0,11):
    print(f"{multiplicador} x {contador} = {multiplicador * contador}")
    
# === while ===
print("\n=== while ===")
opcao = - 1
while opcao != 0:
    opcao = int(input("Digite 1 para sacar, 2 para depositar ou 0 para encerrar: ")) 
    
    if(opcao == 1):
        print("Sacando...")
    elif(opcao == 2):
        print("Depositando...")
    elif(opcao !=0):
        print("Opção inválida")
print("Programa encerrado pelo usuário!")

# === utilizando break ===
print("\n=== utilizando break ===")
opcao - 1

while True:
    numero = int(input("Digite um número inteiro entre 0 e 10: "))
    print(f"O número digitado foi {numero}")
    
    if(numero > 10 or numero < 0):
        print("Numero digitado é inválido!")
    
    if(numero == 10):
        print("Programa encerrado!")
        break
