class Categoria:
    def __init__(self, nome:str, descricao:str=None) -> None:
        self.nome = nome 
        self.descricao = descricao
        
    def __str__(self) -> str:
        return f'Nome: {self.nome} - Descrição: {self.descricao}'
    
class Produto:
    def __init__(self, nome, categoria:Categoria, preco):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        
    def __str__(self) -> str:
        return f'Nome: {self.nome} - Categoria: {self.categoria} - Preço: {self.preco}'
    
class Estoque:
    def __init__(self, produto:Produto, quantidade:int) -> None:
        self.produto = produto
        self.quantidade = quantidade
        
    def __str__(self) -> str:
        return f'Produto: {self.produto} - Quantidade: {self.quantidade}'
    
    
sabonete = Estoque(Produto('Sabonete', Categoria('Higiene', 'produto de higiene pessoal'), 2.50), 100)

print(sabonete)