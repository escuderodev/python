class Restaurante:
    restaurantes = []
    
    def __init__(self, nome: str, categoria: str):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self.restaurantes.append(self)
        
    @classmethod
    def listar_restaurantes(cls):
        print("===== Restaurantes =====")
        for restaurante in cls.restaurantes:
            print(restaurante)
            
    def alterar_situacao_restaurante(self):
        if(self._ativo == False):
            self._ativo = True
        else:
            self._ativo = False
            
    @property
    def nome(self):
        return self._nome

    @property
    def categoria(self):
        return self._categoria

    @property
    def ativo(self):
        return self._ativo

    def __str__(self):
        return f"Nome: {self._nome.ljust(25)} | Categoria: {self._categoria.ljust(25)} | Situação: {self._ativo}"
        

restaurante = Restaurante("praza san lorenzo", "Restaurante")
restaurante_mcdonalds = Restaurante("MCDonalds", "Fast Food")

print()
Restaurante.listar_restaurantes()

restaurante.alterar_situacao_restaurante()
Restaurante.listar_restaurantes()

restaurante.alterar_situacao_restaurante()
Restaurante.listar_restaurantes()