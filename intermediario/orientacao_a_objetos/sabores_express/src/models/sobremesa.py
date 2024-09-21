from models.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome: str, preco: float, tipo: str):
        super().__init__(nome, preco)
        self._tipo = tipo
        
    @property
    def tipo(self):
        return self._tipo    

    def aplicar_desconto(self):
        desconto = (self._preco / 100) * 3
        return self._preco - desconto
    
    def __str__(self) -> str:
        return f'{self._nome} - Tipo: {self._tipo} - R$: {self._preco:.2f}'