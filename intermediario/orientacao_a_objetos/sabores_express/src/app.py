from models.restaurante import Restaurante
from models.prato import Prato
from models.bebida import Bebida
from models.sobremesa import Sobremesa

# instanciando objetos
restaurante = Restaurante('praça san lorenzo', 'Gourmet')
prato = Prato("Parmeggiana de Carne", 80.00, "Parmeggiana de Carne coberto com Queijo Mussarela e Molho de Tomate.")
bebida = Bebida("Coca Cola", 7.50, 350, "ML")
sobremesa = Sobremesa("Bolo Gelado de Coco", 25.00, "Bolo")

# adicionando itens ao cardápio
restaurante.adicionar_item_ao_cardapio(bebida)
restaurante.adicionar_item_ao_cardapio(prato)
restaurante.adicionar_item_ao_cardapio(sobremesa)

# executando a aplicação
def main():
    print()
    restaurante.listar_cardapio()
    print(f"Prato sem desconto R$ {prato.preco:.2f}")
    print(f"Prato com desconto R$ {prato.aplicar_desconto():.2f}")
    print(f"Bebida sem desconto R$ {bebida.preco:.2f}")
    print(f"Bebida com desconto R$ {bebida.aplicar_desconto():.2f}")
    print(f"Sobremesa sem desconto R$ {sobremesa.preco:.2f}")
    print(f"Sobremesa com desconto R$ {sobremesa.aplicar_desconto():.2f}")

if __name__ == '__main__':
    main()
    
# paramos na aula 3.0