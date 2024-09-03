class Estudante:
    escola = "FIAP" #variável de classe

    def __init__(self, nome, ra):
        self.nome = nome #variável de instância
        self.ra = ra #variável de instância

    def __str__(self):
        return f"Nome: {self.nome} | RA: {self.ra} | Escola: {self.escola}"

def mostrar_objetos(*objetos):
    for objeto in objetos:
        print(objeto)

escuderodev = Estudante("Eduardo Escudero", "M458746")

carol = Estudante("karol Tobias", "M778746")
mostrar_objetos(escuderodev, carol)
