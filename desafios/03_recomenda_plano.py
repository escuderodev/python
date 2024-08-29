# === Desafio ===
# Uma empresa de telecomunicações deseja criar uma solução algorítmica que ajude aos seus clientes a escolherem o plano de internet ideal com base em seu consumo mensal de dados. Para a resolução, você pode solicitar ao usuário que insira o seu consumo, sendo este um valor 'float'. Crie uma função chamada recomendar_plano para receber o consumo médio mensal de dados informado pelo cliente, além de utilizar estruturas condicionais para fazer a verificação e retornar o plano adequado.

# Planos Oferecidos:

# - Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB.
# - Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB.
# - Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB.

def recomendar_plano(consumo_mensal):
    if consumo_mensal <= 10:
        print("Plano Essencial Fibra - 50Mbps")
    elif consumo_mensal >= 19 and consumo_mensal < 21:
        print("Plano Prata Fibra - 100Mbps")
    else:
        print("Plano Premium Fibra - 300Mbps")
    
consumo_mensal = float(input("\nInforme o seu consumo médio mensal de dados em GB: "))
recomendar_plano(consumo_mensal)