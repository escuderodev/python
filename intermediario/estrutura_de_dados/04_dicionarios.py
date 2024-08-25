# seclaração de dicionário
pessoa = {"nome": "Eduardo Escudero", "idade": 40}

# podemos acrecentar elementos ao dicionario
pessoa["telefone"] = "11955005284"

print(pessoa)
print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["telefone"])

contatos = {
    "escuderodev@outlook.com": {"nome": "Eduardo Escudero", "idade": 40},
    "carol-tobias@hotmail.com": {"nome": "Carol Tobias", "idade": 41},
    "juan@outlook.com": {"nome": "Juan Tobias Escudero", "idade": 10},
    "alicia@outlook.com": {"nome": "Alicia Valentina Tobias Escudero", "idade": 5},
}
print(contatos)
print(contatos["escuderodev@outlook.com"]["idade"])

# iterando sobre o dicionario contatos
for contato in contatos:
    print(contato, contatos[contato])
    
for contato in contatos:
    print(contato, contatos[contato]["nome"])
    
# métodos da classe dicionario
contatos.clear() # apaga o dicionário
copia = contatos.copy() # retorna uma cópia do dicionário
contatos.fromkeys("profissao") # cria novas chaves
contatos.get("time") # permite consultar por uma chave inexistente sem parar a aplicação
contatos.get("time") # por padrão retorna None
contatos.get("time", {}) # {}
contatos.items() # retorna a lista de itens do dicionário
contatos.keys() # retorna apenas as chaves, sem seus valores
contatos.setdefault("pais", "Brasil") # define um valor padrão caso a chave não seja informada
contatos.update({"escuderodev@outlook.com": {"nome": "Eduardo Escudero", "idade": 40}}) # permite atualizar um elemento do dicionário
"escuderodev@outlook.com" in contatos # retorna True
del contatos[["escuderodev@outlook.com"]["telefone"]] # remove o atributo de uma chave
del contatos[["escuderodev@outlook.com"]] # remove a chave por completo
