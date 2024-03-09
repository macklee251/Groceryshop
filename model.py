from datetime import datetime, date
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
    
    
class Venda:
    def __init__(self, produto:Produto, vendedor, comprador, quantidade:int, date=datetime.now()) -> None:
        self.produto = produto
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidade = quantidade
        self.date = date
    
    def __str__(self) -> str:
        return f'Produto: {self.produto} - Vendedor: {self.vendedor} - Comprador: {self.comprador} - Quantidade: {self.quantidade} - Data: {self.date}'
        
class Fornecedor:
    def __init__(self, nome, cnpj, telefone, categoria: Categoria) -> None:
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.categoria = categoria
        
class Pessoa:
    def __init__(self, nome, telefone, cpf, email, endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email
        self.endereco = endereco

class Funcionario(Pessoa):
    def __init__(self, nome, clt, telefone, cpf, email, endereco) -> None:
        self.clt = clt
        super().__init__(nome, telefone, cpf, email, endereco)
        
        
