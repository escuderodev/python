# Iterador para ler um arquivo externo
class FileIterator:
    def __init__(self, file_name):
        self.file = open(file_name)

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if line != '':
            return line
        else:
            self.file.close()
            raise StopIteration

# utilizando o fileiterator
for line in FileIterator('iterator.txt'):
    print(line)

# Iterador para ler uma lista de dados
class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero
        except IndexError:
            raise StopIteration

for i in MeuIterador(numeros=[1,5,0,2,3,6,5,4,52,14,10,100]):
    print(i)