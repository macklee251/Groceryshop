from model import Categoria
from dal import CategoriaDal
from globalSettings import text_formatter
from globalSettings import checking_duplicity

class CategoriaController:
    @classmethod
    def register(cls, name:str, description:str=None):
        name = text_formatter(name)
        description = text_formatter(description)
        if isinstance(name, str) and (isinstance(description, str) or description == None) and not checking_duplicity(name, description):
            categoria = Categoria(name, description)
            try:
                CategoriaDal.write(categoria)
                return True
            except:
                return False        
            
CategoriaController().register('limpea')
