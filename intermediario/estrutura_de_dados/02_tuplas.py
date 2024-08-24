estados = ("sp", "rj", "mg", "rs", "am",)
pais = ("brasil",)
numeros = (1, 2, 3, 4, 5,)

# a forma de acessar os indices de uma tupla é igual ao de uma lista
print(estados[2])
print(pais[0])
print(numeros[2])

# metodos da classe tuple
print(numeros.count(3)) # conta quantas vezes o elemento existe na tupla
print(numeros.index(2)) #retorna o indice da posição do elemento na tupla
print(numeros.__contains__(4)) # verifica se um elemento está presente na tupla
