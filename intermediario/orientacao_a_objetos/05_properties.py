class Pessoa:
    def __init__(self, nome: str, ano_nascimento: int, profissao: str):
        self._nome = nome
        self._ano_nascimento = ano_nascimento
        self._profissao = profissao

    @property
    def nome(self):
        return self._nome

    @property
    def ano_nascimento(self):
        return self._ano_nascimento

    @property
    def profissao(self):
        return self._profissao

    def calcular_idade(self, ano_atual: int):
        return ano_atual - self._ano_nascimento

    def __str__(self):
        return f"Nome: {self._nome} | Data de Nascimento: {self._ano_nascimento} | Profissão: {self._profissao}"

pessoa = Pessoa("Eduardo Escudero", 1984, "Dev")
print(pessoa)
idade = pessoa.calcular_idade(2024)
print(f"Você tem {idade} anos de idade.")
print(pessoa.nome)
print(pessoa.ano_nascimento)
print(pessoa.profissao)