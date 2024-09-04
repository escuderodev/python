from abc import ABC, abstractmethod

class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("TV ligando...")
        print("Ligado!")

    def desligar(self):
        print("TV desligando...")
        print("Desligado!")

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ar Condicionado ligando...")
        print("Ligado!")

    def desligar(self):
        print("Ar Condicionado desligando...")
        print("Desligado!")

    def aumentar_temperatura(self):
        print("Aumentando a temperatura...")

    def diminuir_temperatura(self):
        print("Diminuindo a temperatura...")

print()
controle_tv = ControleTV()
controle_tv.ligar()
controle_tv.desligar()

print()
controle_ar_condigionado = ControleArCondicionado()
controle_ar_condigionado.ligar()
controle_ar_condigionado.desligar()
controle_ar_condigionado.aumentar_temperatura()
controle_ar_condigionado.diminuir_temperatura()