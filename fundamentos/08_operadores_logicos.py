age = 17
accompanied = False

if(age >= 18 or accompanied):
    print("Você é maior de idade ou está acompanhado")
else:
    print("Você é menor de idade e está desacompanhado")
    
team = "santos"

if(team != "corinthians" and team != "são paulo" and team != "santos" and team == "palmeiras"):
    print(f"Seu time é {team} e ele não tem mundial!")
else:
    print(f"Seu time é {team} e ele tem mundial!")