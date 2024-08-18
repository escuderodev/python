# verifica se dois objetos ocupam a mesma região de memória

curso = "python"
novo_curso = curso
mais_um_curso = "javascript"

print(novo_curso is curso)
print(mais_um_curso is curso)
print(curso is not mais_um_curso)