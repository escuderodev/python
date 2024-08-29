# Desafio
# Imagine que você trabalha para uma empresa de telecomunicações e é responsável por validar se um número de telefone fornecido pelo cliente está em um formato correto. Para garantir a precisão dos registros, é essencial que os números de telefone estejam no formato padrão. Desenvolva uma função programa que valide se um número de telefone tem o formato correto.

# Formato esperado:
# O formato aceito para números de telefone é: (XX) 9XXXX-XXXX, onde X representa um dígito de 0 a 9. Lembre-se de respeitar os espaços entre os números quando preciso.

# Entrada
# Uma string representando o número de telefone.

# Saída
# Uma mensagem indicando se o número de telefone é válido ou inválido.

import re

# Expressão regular para validar o formato (xx) xxxxx-xxxx
telefone_regex = r'^\(\d{2}\) \d{5}-\d{4}$'

# Função para validar o telefone
def validar_telefone(telefone):
    return re.match(telefone_regex, telefone) is not None

# Exemplos de uso
print(validar_telefone("(12) 34567-8901"))  # True
print(validar_telefone("(12) 3456-7890"))   # False
print(validar_telefone("(123) 45678-9012")) # False
print(validar_telefone("12 34567-8901"))    # False
