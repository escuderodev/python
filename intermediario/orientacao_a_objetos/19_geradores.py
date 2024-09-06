from datetime import datetime
from time import timezone


def meu_gerador(list):
    for item in list:
        yield item

nomes = ["Eduardo", "Carol", "Juan", "Alicia", "Valmir", "Fátima", "Daniel"]
numeros = [1,2,3,4,5,6,7,8,9,0]

for i in meu_gerador(nomes):
    print(i)

for i in meu_gerador(numeros):
    print(i)

# gerador deve ser usado quando o código for simples
# iterador deve ser usado quando o código for complexo

print(datetime.now())