def duplicar(func):
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        
    return envelope

@duplicar
def aprender(tecnologia: str):
    print(f"Estou aprendendo {tecnologia}")
    
aprender("Python")