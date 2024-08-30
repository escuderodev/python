class Animal:
    def __init__(self, raca: str, sexo: str, cor: str):
        self.raca = raca
        self.sexo = sexo
        self.cor = cor

    def dormir(self):
        print(f"{self.raca} dormindo...")
    
    def acordar(self):
        print(f"{self.raca} acordando...")

class Ave(Animal):
    def __init__(self, raca: str, sexo: str, cor: str):
        super().__init__(raca, sexo, cor)
        
    def voar(self):
        print(f"{self.raca} voando...")
        
class Mamifero(Animal):
    def __init__(self, raca: str, sexo: str, cor: str):
        super().__init__(raca, sexo, cor)
    
    def mamar(self):
        print(f"{self.raca} filhote mamando...")
        
class Cachorro(Mamifero):
    def __init__(self, raca: str, sexo: str, cor: str):
        super().__init__(raca, sexo, cor)
    
    def latir(self):
        print(f"{self.raca} cachorro latindo...")
    
class Gato(Mamifero):
    def __init__(self, raca: str, sexo: str, cor: str):
        super().__init__(raca, sexo, cor)
    
    def miar(self):
        print(f"{self.raca} gato miando...")

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, raca: str, sexo: str, cor: str):
        super().__init__(raca, sexo, cor)
    
    def pular(self):
        print(f"{self.raca} pulando...")
        
cachorro = Cachorro("Puddle", "Feminino", "Preto")
gato = Gato("Ciberiano", "Feminino", "Branco")
ornitorrinco = Ornitorrinco("Ornitorrinco", "Masculino", "Marrom")

cachorro.acordar()
cachorro.dormir()
cachorro.latir()

gato.acordar()
gato.dormir()
gato.miar()

ornitorrinco.acordar()
ornitorrinco.dormir()
ornitorrinco.pular()
ornitorrinco.voar()