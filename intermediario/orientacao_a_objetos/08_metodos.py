class Pessoa:
    def __init__(self, nome: str = None, idade: int = None):
        self._nome = nome
        self._idade = idade

    def __str__(self):
        return f"Meu nome é {self._nome} e tenho {self._idade} anos de idade."

    @classmethod
    def criar_pessoa_com_data_de_nascimento(cls, nome: str, ano_de_nascimento: int,):
        idade = 2024 - ano_de_nascimento
        return cls(nome, idade)

    @staticmethod
    def e_maior_de_idade(idade):
        return idade >= 18

pessoa = Pessoa("Eduardo Escudero", 40)
print(pessoa)

karol = Pessoa.criar_pessoa_com_data_de_nascimento("Karol Tobias", 1983)
print(karol)

print(Pessoa.e_maior_de_idade(15))
print(Pessoa.e_maior_de_idade(18))
print(Pessoa.e_maior_de_idade(25))
