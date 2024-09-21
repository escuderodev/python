from models.restaurante import Restaurante
from models.prato import Prato
from models.bebida import Bebida

restaurante = Restaurante('praça san lorenzo', 'Gourmet')
prato = Prato("Parmeggiana de Carne", 80.00, "Parmeggiana de Carne coberto com Queijo Mussarela e Molho de Tomate.")
bebida = Bebida("Coca Cola", 7.50, 0.350)

def main():
    print()
    print(restaurante)
    print(prato)
    print(bebida)

if __name__ == '__main__':
    main()