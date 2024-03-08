from model import Categoria

class CategoriaDal:
    @classmethod
    def write(cls, categoria: Categoria) -> None:
        with open ('categorias.txt', 'a') as file:
            file.write(f'{categoria.name},{categoria.description}\n')
            
    @classmethod
    def read(cls):
        category = []
        with open('categorias.txt', 'r') as file:
            for row in file:
                name, description = row.strip().split(',')
                category.append(Categoria(name, description))
        return category