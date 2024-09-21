class Veiculo:
    def __init__(self, marca: str, modelo: str, cor: str, ano: str):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = int(ano)
        
    def acelerar(self):
        print("Acelerando...")
    
    def frear(self):
        print("Parando...")
    
    def __str__(self) -> str:
        return f"\nMarca: {self.marca} | Modelo: {self.modelo} | Cor: {self.cor} | Ano de Fabricação: {self.ano}"
    
class Carro(Veiculo):
    def abastecer(self):
        print("Carro abastecendo...")

fiesta = Carro("Ford", "Fiesta Hatch 2014", "Preto", 2014)
print(fiesta)
fiesta.acelerar()
fiesta.frear()
fiesta.abastecer()