# Data as object
from Models import *

class DaoCategoria:
    @classmethod
    def salvar(cls, categoria:Categoria):
        with open('categorias.txt', 'a') as file:
            file.write(f'{categoria.nome},{categoria.descricao}\n')
            
    @classmethod
    def ler(cls):
        categorias = []
        with open('categorias.txt', 'r') as file:
            for line in file:
                data = line.strip().split(',', 1)
                nome = data[0]
                descricao = data[1] if len(data) > 1 else ""
                categorias.append(Categoria(nome, descricao))
        return categorias
    
    
if __name__=="__main__":
    print(DaoCategoria.ler())