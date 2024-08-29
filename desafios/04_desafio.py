# Desafio
# Você foi designado para desenvolver um programa para gerenciar os equipamentos de uma empresa. O objetivo é criar uma solução que permita aos usuários inserir informações sobre os equipamentos que serão cadastrados na rede, em seguida, exibir essa lista de equipamentos. Crie uma Lista para armazenar esses equipamentos e depois um loop para solicitar ao usuário inserir até três equipamentos.

# Entrada
# O programa solicitará ao usuário que insira uma lista com três equipamentos para adicionar a rede.

# Saída
# Após a entrada dos itens, o programa exibirá a lista de equipamentos inseridos pelo usuário. Cada equipamento será listado com um prefixo ( - ) de marcação para melhor organização.

itens = []

while len(itens) < 3:
    equipamento = input("\nDigite o equipamento: ")
    itens.append(equipamento)
    
print("\n=== lista de itens ===")
for item in itens:
    print(f"- {item}")