class Insumo:
    def __init__(self, nome: str, tamanho_embalagem: int, valor_embalagem: float):
        self._nome = nome
        self._tamanho_embalagem = tamanho_embalagem
        self._valor_embalagem = valor_embalagem
        self._valor_unitario = valor_embalagem / tamanho_embalagem

    @property
    def nome(self):
        return self._nome

    @property
    def tamanho_embalagem(self):
        return self._tamanho_embalagem

    @property
    def valor_embalagem(self):
        return self._valor_embalagem

    @property
    def valor_unitario(self):
        return self._valor_unitario

    def __str__(self):
        return f"""
        === Insumo ===
        Descrição: {self._nome}
        Tamanho da Embalagem: {self._tamanho_embalagem}
        Valor da Embalagem R$: {self._valor_embalagem:.2f}
        Valor Unitário R$: {self._valor_unitario:.2f}
        """

class ProdutoInsumo:
    def __init__(self, nome_insumo: str, valor_unitario: float, quantidade: int):
        self.nome_insumo = nome_insumo
        self.valor_unitario = valor_unitario
        self.quantidade = quantidade

class Produto:
    def __init__(self, nome: str):
        self._nome = nome
        self.insumos = []
        self._valor = 0.00

    @property
    def nome(self):
        return self._nome

    @property
    def valor(self):
        return self._valor

    def adicionar_insumo(self, produto_insumo):
        self.insumos.append({
            "nome_insumo": produto_insumo.nome_insumo,
            "valor_unitario": produto_insumo.valor_unitario,
            "quantidade": produto_insumo.quantidade
        })
        valor_insumo = produto_insumo.valor_unitario * produto_insumo.quantidade
        self._valor += valor_insumo

    def __str__(self):
        return f"""
        Produto: {self.nome}
        Insumos: {self.insumos}
        Valor R$: {self._valor:.2f}
        """

xilitol = Insumo("Xilitol",500, 70.00)
cacau = Insumo("Cacau 100%", 1000, 50.00)
leite_sem_lactose = Insumo("Leite sem Lactose", 1000, 5.70)
print(xilitol)
print(cacau)
print(leite_sem_lactose)

produto_insumo1 = ProdutoInsumo(xilitol.nome, xilitol.valor_unitario, 25)
produto_insumo2 = ProdutoInsumo(cacau.nome, cacau.valor_unitario, 350)
produto_insumo3 = ProdutoInsumo(leite_sem_lactose.nome, leite_sem_lactose.valor_unitario, 1000)

produto = Produto("Brigadeiro 100% Cacau")

produto.adicionar_insumo(produto_insumo1)
produto.adicionar_insumo(produto_insumo2)
produto.adicionar_insumo(produto_insumo3)

print(produto)