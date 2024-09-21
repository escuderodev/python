from models.restaurante import Restaurante
from models.prato import Prato
from models.bebida import Bebida

# instanciando objetos
restaurante = Restaurante('praça san lorenzo', 'Gourmet')
prato = Prato("Parmeggiana de Carne", 80.00, "Parmeggiana de Carne coberto com Queijo Mussarela e Molho de Tomate.")
bebida = Bebida("Coca Cola", 7.50, 350, "ML")

# adicionando itens ao cardápio
restaurante.adicionar_item_ao_cardapio(bebida)
restaurante.adicionar_item_ao_cardapio(prato)

# executando a aplicação
def main():
    print()
    print(restaurante)
    restaurante.listar_cardapio()

if __name__ == '__main__':
    main()