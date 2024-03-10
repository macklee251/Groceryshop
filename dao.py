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
                nome, descricao = line.strip().split(',')
                categorias.append(Categoria(nome, descricao))
        return categorias
    
    
if __name__=="__main__":
    print(DaoCategoria.ler())