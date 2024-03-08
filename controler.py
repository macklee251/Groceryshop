from model import Categoria
from dal import CategoriaDal
from globalSettings import text_formatter

class CategoriaControler:
    @classmethod
    def register(cls, name:str, description:str=None):
        if isinstance(name, str) and (isinstance(description, str) or description == None):
            categoria = Categoria(text_formatter(name) , text_formatter(description))
            try:
                CategoriaDal.write(categoria)
                return True
            except:
                return False
            
            
CategoriaControler().register('limpesa', 'limpesa    de  casa')
        