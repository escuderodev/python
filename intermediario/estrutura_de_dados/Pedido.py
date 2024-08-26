class Insumo:
    def __init__(self,nome, quantidade_embalagem, valor_embalagem):
        self.nome = nome
        self.quantidade_embalagem = quantidade_embalagem
        self.valor_embalagem = valor_embalagem
        self.valor_unitario = valor_embalagem / quantidade_embalagem
        
class ItemProduto:
    def __init__(self, nome, valor_unitario, quantidade):
        self.nome = nome
        self.valor_unitario = valor_unitario
        self.quantidade = quantidade
        
class Produto:
    def __init__(self, nome):
        self.nome = nome
        self.itens = []
        self.valor = 0.00
        
    def adicionar_item(self, item_produto):
        self.itens.append(item_produto)
        self.valor = self.valor + (item_produto.valor_unitario * item_produto.quantidade)
        
    def exibir_produto(self):
        print(f"Produto: {self.nome}")
        print("=== Insumos ===")
        for item_produto in self.itens:
            valor_item_receita = item_produto.valor_unitario * item_produto.quantidade
            print(f"Item: {item_produto.nome} | Qtd: {item_produto.quantidade} | RS: {valor_item_receita:.2f}")
        print(f"Custo de Fabricação R$: {self.valor:.2f}")
        
# criando insumos
chocolate = Insumo("Chocolate 100% Cacau",1000,50.00)
xilitol = Insumo("Xilitol", 1000, 65.00)
leite_em_po = Insumo("Leite em Pó sem Lactose", 1000, 5.50)

# criando item_produto
item_chocolate = ItemProduto(chocolate.nome, chocolate.valor_unitario, 250)
item_xilitol = ItemProduto(xilitol.nome, xilitol.valor_unitario, 25)
item_leite_em_po = ItemProduto(leite_em_po.nome, leite_em_po.valor_unitario, 1000)

# criando produto
brigadeiro = Produto("Brigadeiro de Chocolate 100% Cacau")
brigadeiro.adicionar_item(item_chocolate)
brigadeiro.adicionar_item(item_xilitol)
brigadeiro.adicionar_item(item_leite_em_po)
brigadeiro.exibir_produto()
