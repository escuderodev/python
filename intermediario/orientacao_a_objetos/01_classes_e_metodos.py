class Bicicleta:
    def __init__(self, cor: str, modelo: str, ano: int, valor: float):
        self.cor = cor
        self.modelo = modelo
        self.ano = int(ano)
        self.valor = float(valor)
            
    def businar(self):
        print("Bicileta businando...")
    
    def parar(self):
        print("Bicileta parando...")
    
    def correr(self):
        print("Bicileta acelerando...")
        
    def get_cor(self):
        return self.cor
    
    def get_modelo(self):
        return self.modelo
    
    def get_ano(self):
        return self.ano
    
    def get_valor(self):
        return self.valor
    
    def __str__(self):
        return f"Bicicleta - Modelo: {self.modelo} | Cor: {self.cor} | Ano de Fabricação: {self.ano} | Valor R$: {self.valor:.2f}"
    
    # def __str__(self):
    #     return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
    def __del__(self):
        print("Removendo a instãncia da classe...")
        # metodo declarado apenas quando quisermos fazer algo antes que o objeto seja destruído
        
speed = Bicicleta("Preta", "Speed", 2024, 2500.00)
print(speed)
speed.businar()
speed.correr()
speed.parar()
print(speed.get_modelo())
print(speed.get_cor())
print(speed.get_ano())
print(f"{speed.get_valor():.2f}")
