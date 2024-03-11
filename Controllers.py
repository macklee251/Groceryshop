from Models import *
from DAO import * 

class ControllerCategoria():
    @classmethod
    def cadastrarCategoria(cls, nome:str, descricao:str=None):
        try:
            for categoria in DaoCategoria.lerCategoria():
                if nome == categoria.nome:
                    return None
            else:
                categoria = Categoria(nome, descricao)
                DaoCategoria.salvarCategoria(categoria)
                return categoria
        except:
            return None
        
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
        
class ControllerProduto():
    @classmethod
    def cadastrarProduto(cls, nome:str, categoria:str, preco:str):
        try:
            for produto in DaoProduto.lerProduto():
                if nome == produto.nome:
                    return None
            else:
                produto = Produto(nome, categoria, preco)
                DaoProduto.salvarProduto(produto)
                return produto
        except:
            return None
        
    @classmethod
    def removerProduto(cls, nome:str):
        produtos = DaoProduto.lerProduto()
        for produto in produtos:
            if nome == produto.nome:
                produtos.remove(produto)
                with open('produtos.txt', 'w') as file:
                    for produto in produtos:
                        file.write(f'Nome: {produto.nome}, Categoria: {produto.categoria}, Preço: {produto.preco}\n')
                return produto
        else:
            return None
                
class ControllerEstoque():
    @classmethod
    def cadastrarEstoque(cls, produto:str, quantidade:int):
        try:
            for estoque in DaoEstoque.lerEstoque():
                if produto == estoque.produto:
                    return None
            else:
                estoque = Estoque(produto, quantidade)
                DaoEstoque.salvarEstoque(estoque)
                return estoque
        except:
            return None
        
    @classmethod
    def removerEstoque(cls, produto:str):
        estoques = DaoEstoque.lerEstoque()
        for estoque in estoques:
            if produto == estoque.produto:
                estoques.remove(estoque)
                with open('estoque.txt', 'w') as file:
                    for estoque in estoques:
                        file.write(f'Produto: {estoque.produto}, Quantidade: {estoque.quantidade}\n')
                return estoque
        else:
            return None
        
class ControllerVenda():
    @classmethod
    def cadastrarVenda(cls, produto:str, vendedor:str, comprador:str, quantidade:int, date=datetime.now()):
        try:
            venda = Venda(produto, vendedor, comprador, quantidade, date)
            DaoVenda.salvarVenda(venda)
            return venda
        except:
            return None
        
    @classmethod
    def removerVenda(cls, produto:str):
        vendas = DaoVenda.lerVenda()
        for venda in vendas:
            if produto == venda.produto:
                vendas.remove(venda)
                with open('vendas.txt', 'w') as file:
                    for venda in vendas:
                        file.write(f'Produto: {venda.produto}, Vendedor: {venda.vendedor}, Comprador: {venda.comprador}, Quantidade: {venda.quantidade}, Data: {venda.date}\n')
                return venda
        else:
            return None
        
class ControllerFornecedor():
    @classmethod
    def cadastrarFornecedor(cls, nome, cnpj, telefone, categoria: Categoria):
        try:
            fornecedor = Fornecedor(nome, cnpj, telefone, categoria)
            DaoFornecedor.salvarFornecedor(fornecedor)
            return fornecedor
        except:
            return None
        
    @classmethod
    def removerFornecedor(cls, nome):
        fornecedores = DaoFornecedor.lerFornecedor()
        for fornecedor in fornecedores:
            if nome == fornecedor.nome:
                fornecedores.remove(fornecedor)
                with open('fornecedores.txt', 'w') as file:
                    for fornecedor in fornecedores:
                        file.write(f'Nome: {fornecedor.nome}, CNPJ: {fornecedor.cnpj}, Telefone: {fornecedor.telefone}, Categoria: {fornecedor.categoria}\n')
                return fornecedor
        else:
            return None

class ControllerPessoa():
    @classmethod
    def cadastrarPessoa(cls, nome, telefone, cpf, email, endereco):
        try:
            pessoa = Pessoa(nome, telefone, cpf, email, endereco)
            DaoPessoa.salvarPessoa(pessoa)
            return pessoa
        except:
            return None
        
    @classmethod
    def removerPessoa(cls, nome):
        pessoas = DaoPessoa.lerPessoa()
        for pessoa in pessoas:
            if nome == pessoa.nome:
                pessoas.remove(pessoa)
                with open('pessoas.txt', 'w') as file:
                    for pessoa in pessoas:
                        file.write(f'Nome: {pessoa.nome}, Telefone: {pessoa.telefone}, CPF: {pessoa.cpf}, Email: {pessoa.email}, Endereço: {pessoa.endereco}\n')
                return pessoa
        else:
            return None

class ControllerFuncionario():
    @classmethod
    def cadastrarFuncionario(cls, nome, clt, telefone, cpf, email, endereco):
        try:
            funcionario = Funcionario(nome, clt, telefone, cpf, email, endereco)
            DaoFunionario.salvarFuncionario(funcionario)
            return funcionario
        except:
            return None
    
    @classmethod   
    def removerFuncionario(cls, nome):
        funcionarios = DaoFunionario.lerFuncionario()
        for funcionario in funcionarios:
            if nome == funcionario.nome:
                funcionarios.remove(funcionario)
                with open('funcionarios.txt', 'w') as file:
                    for funcionario in funcionarios:
                        file.write(f'Nome: {funcionario.nome}, CLT: {funcionario.clt}, Telefone: {funcionario.telefone}, CPF: {funcionario.cpf}, Email: {funcionario.email}, Endereço: {funcionario.endereco}\n')
                return funcionario
        else:
            return None
    
    
            
if __name__ == "__main__":
    print(ControllerProduto.cadastrarProduto('Arroz', 'Alimento', 5.00))