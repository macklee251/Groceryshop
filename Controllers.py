from Models import *
from DAO import * 

class ControllerCategoria():
    @classmethod
    def cadastrar(cls, nome:str, descricao:str=None):
        if nome:
            print("ok")
        else:
            print('Nome inválido')
            
            
ControllerCategoria().cadastrar('Bebidas')