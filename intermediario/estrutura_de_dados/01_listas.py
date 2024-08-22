def exibir_mensagem(mensagem):
    print(f"\n=== {mensagem} ===")

exibir_mensagem("Acessando uma posição da lista")
nomes = ["Eduardo", "Carol", "Juan", "Alícia"]
print(nomes[1])

exibir_mensagem("Percorrendo uma lista com For")
for nome in nomes:
    print(nome)
    
for indice,nome in enumerate(nome):
    print(f"{indice} - {nome}")
    
exibir_mensagem("Adicionando um elemento à lista")
nomes.append("Valmir")
print(nomes)

exibir_mensagem("Listas aninhadas")
produtos = ["Brigadeiro", "Pudim", "Bolo", "Coxinha"]
valores = [60.00, 35.00, 70.00, 25.00]
produtos_com_precos = [produtos, valores]
print(produtos)
print(valores)
print(produtos_com_precos)
print(f"Produto: {produtos_com_precos[0][1]} R$ {produtos_com_precos[1][1]}")
# quando pegamos uma posição negativa nomes[-1] estamos pegando o último elemento da lista

exibir_mensagem("Fatiamento em Listas")
linguagem = ["p","y","t","h","o","n"]
print(linguagem)
print(linguagem[0])
print(linguagem[2:])
print(linguagem[:2])
print(linguagem[1:3])
print(linguagem[0:3:2])
print(linguagem[::])
print(linguagem[::-1])

exibir_mensagem("Comprimindo Listas")
numeros = [1,2,3,4,5,6,7,8,9,10,5]
pares = [numero for numero in numeros if numero % 2 == 0]
print(numeros)
print(pares)

exibir_mensagem("Elevando os números de uma lista ao quadrado")
numeros_ao_quadrado = [numero ** 2 for numero in numeros]
print(numeros_ao_quadrado)

exibir_mensagem("Testando os métodos da classe list")
disciplinas = ["python", "javascript", "typescript", "java", "c#"]
print(disciplinas)
disciplinas.append("php") # add um item a lista
numeros.count(5) #conta quantas vezes um determinado está presente em uma lista 
novas_disciplinas = disciplinas.copy() # retorna uma cópia da lista original
disciplinas.extend(["nodejs","mongodb"]) # permite add mais de um melemento à lista
disciplinas.index("python") # retorna o indice da primeira ocorrência correspondente ao elemento pesquisado
disciplinas.pop() # retira da lista o último elemento exceto quando informado o indice
disciplinas.remove("nodejs") # retira da lista o objeto informado
disciplinas.reverse() # inverte a ordem dos elementos da lista
disciplinas.sort() # ordena a lista de acordo com os parâmetros informados
disciplinas.sort(reverse=True) # ordena a lista de acordo com os parâmetros informados
disciplinas.sort(key=lambda x: len(x)) # ordena a lista de acordo com os parâmetros informados
disciplinas.sort(key=lambda x: len(x), reverse=True) # ordena a lista de acordo com os parâmetros informados
len(disciplinas) # retorna o tamanho da lista
disciplinas.clear() # apaga o conteúdo da lista

sorted(disciplinas) # método builtin do python que ordena uma lista