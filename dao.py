# Data as object
from model import *

class daoCategoria():
    @classmethod
    def salvar(cls, file_name, obj):
        with open(f'{file_name}.txt', 'a') as file:
            for attr, value in obj.__dict__.items():
                file.write(f'{attr}: {value},')
            file.write('\n')
            
            
daoCategoria().salvar('venda', Venda(Produto('Arroz', Categoria('Alimento', 'Grão'), 5), 'João', 'Maria', 5))