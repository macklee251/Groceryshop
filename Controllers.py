from Models import *
from DAO import * 

class ControllerCategoria():
    @classmethod
    def cadastrar(cls, nome:str, descricao:str=None):
        if nome:
            try:
                categoria = Categoria(nome, descricao)
                DaoCategoria.salvar(categoria)
                return True
            except:
                return False
            
ControllerCategoria.cadastrar('Bebidas', 'Refrigerantes, sucos, água')