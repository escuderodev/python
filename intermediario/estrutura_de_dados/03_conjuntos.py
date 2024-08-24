# conjunto funciona semelhante a uma lista, porém ele elimina duplicidades
# ele pode receber como parâmetro listas e tuplas
# não guarda a ordem dos indices

# recebendo dados pelo construtor set()
numeros = set([1,2,3,4,5,4])
fruta = set(("abacaxi"))
carros = set(("palio","gol","celta","palio"))

print(numeros)
print(fruta)
print(carros)

# recebendo dados sem construtor
linguagens = {"python", "javascript", "typescript", "java", "python"}
print(linguagens)
novos_carros = {"ferrari", "lamborgni", "ferrari", "porche"}
print(novos_carros)

# para acessar elementos dentro do set (conjunto) devemos antes convertê-lo para lista ou tupla
numbers = {1,2,3,4,5,4,3}
print(numbers)
numbers_list = list(numbers)
print(numbers_list)
mumbers_tuple = tuple(numbers)
print(mumbers_tuple)

times = {"Corinthians", "Palmeiras", "Santos", "São Paulo"}
for time in times:
    print(time)
    
# caso seja necessário descobrir o indice atual do elemento, podemos usar enumerate
for indice, time in enumerate(times):
    print(f"{indice}: {time}")
    
# metodos da classe set
bloco_a = {1,2,3}
bloco_b = {1,2,3,4,5}
print(bloco_a.union(bloco_b)) # unir os blocos e eliminar duplicidade
print(bloco_a.intersection(bloco_b)) # pegar apenas os elementos em comum
print(bloco_a.difference(bloco_b)) # retorna tudo que tem em a e não tem em b
print(bloco_b.difference(bloco_a)) # retorna tudo que tem em b e não tem em a
print(bloco_a.symmetric_difference(bloco_b)) # retorna todos os elementos que não são comuns aos blocos
print(bloco_a.issubset(bloco_b)) # verifica se todos os elementos de um bloco estão presentes em outro bloco (objeto filho)
print(bloco_a.issuperset(bloco_b)) # verifica se um bloco contem todos os elementos de outro bloco dentro dele (objeto pai)
print(bloco_a.isdisjoint(bloco_b)) # valida se os elementos do bloco a são diferentes do bloco b
print(bloco_a.add(7)) # add elementos em um set (conjunto)
bloco_a.clear() # limpa o set
bloco_a.copy() # retorna uma copia do set
bloco_a.discard(2) # remove um item do set
bloco_a.pop() # remove o primeiro item do set
bloco_a.remove(2) # remove o item informado
1 in bloco_a # se o 1 existir em bloco_a, retorna True
