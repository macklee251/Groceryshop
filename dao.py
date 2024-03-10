# Data as object
from Models import *

class DaoCategoria:
    @classmethod
    def salvar(cls, categoria:Categoria):
        with open('categorias.txt', 'a') as file:
            file.write(f'Nome: {categoria.nome}, Descrição: {categoria.descricao}\n')
            
    @classmethod
    def ler(cls):
        categorias = []
        with open('categorias.txt', 'r') as file:
            for line in file:
                nome = line.strip().split('Nome: ')[1].split(', Descrição:')[0]
                descricao = line.strip().split('Descrição: ')[1]
                categorias.append(Categoria(nome, descricao))
        return categorias

    
if __name__=="__main__":
    print(DaoCategoria().ler()[0].nome)