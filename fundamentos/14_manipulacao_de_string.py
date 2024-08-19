palavra = "TesTe"
print(palavra.upper())
print(palavra.lower())
print(palavra.title())

linguagem = "   Python   "
print(linguagem.strip())  # remove espaços em branco, tanto no início quanto no fim
print(linguagem.lstrip()) # remove espaços em branco, no início
print(linguagem.rstrip()) # remove espaços em branco, no fim

curso = "Python"
print(curso.center(10, "#")) # centraliza o conteúdo e insere um item no iício e no fim
print("-".join(curso))       # separa os caracteres e insere um item entre eles

