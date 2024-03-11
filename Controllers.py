from Models import *
from DAO import * 

class ControllerCategoria():
    @classmethod
    def cadastrarCategoria(cls, nome:str, descricao:str=None):
        for categoria in DaoCategoria.ler():
            if nome == categoria.nome:
                return None
        else:
            categoria = Categoria(nome, descricao)
            DaoCategoria.salvar(categoria)
            return categoria
        
    @classmethod
    def removerCategoria(cls, nome:str):
        categorias = DaoCategoria.ler()
        for categoria in categorias:
            if nome == categoria.nome:
                categorias.remove(categoria)
                with open('categorias.txt', 'w') as file:
                    for categoria in categorias:
                        file.write(f'Nome: {categoria.nome}, Descrição: {categoria.descricao}\n')
                return categoria
        else:
            return None
        

            
if __name__ == "__main__":
    print(ControllerCategoria.removerCategoria("Bebidas"))