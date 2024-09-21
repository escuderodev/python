from models.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome: str, preco: float, descricao: str):
        super().__init__(nome, preco)
        self._descricao = descricao
        
    @property
    def descricao(self):
        return self._descricao
    
    def aplicar_desconto(self):
        desconto = (self._preco / 100) * 5
        return self._preco - desconto
        
    def __str__(self) -> str:
        return f'{self._nome} - Descrição: {self._descricao} - R$ {self._preco:.2f}'