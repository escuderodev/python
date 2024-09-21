from models.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome: str, preco: float, tamanho: float):
        super().__init__(nome, preco)
        self._tamanho = tamanho
        
    @property
    def tamanho(self):
        return self._tamanho    
    
    def __str__(self) -> str:
        return f'Bebida: {self._nome} - Tamanho: {self._tamanho} - R$: {self._preco:.2f}'