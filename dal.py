from model import Categoria

class CategoriaDal:
    @classmethod
    def write(cls, categoria: Categoria) -> None:
        with open ('categorias.txt', 'a') as file:
            file.write(f'{categoria.name},{categoria.description}\n')
            
    @classmethod
    def read(cls):
        categoria = []
        with open('categorias.txt', 'r') as file:
            for linha in file:
                name, description = linha.strip().split(',')
                categoria.append(Categoria(name, description))
        return categoria