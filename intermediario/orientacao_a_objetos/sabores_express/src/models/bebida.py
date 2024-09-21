from models.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome: str, preco: float, tamanho: int, unidade_medida: str):
        super().__init__(nome, preco)
        self._tamanho = tamanho
        self._unidade_medida = unidade_medida
        
    @property
    def tamanho(self):
        return self._tamanho    
    
    @property
    def unidade_medida(self):
        return self._unidade_medida
    
    def __str__(self) -> str:
        return f'{self._nome} - Tamanho: {self._tamanho}{self._unidade_medida} - R$: {self._preco:.2f}'