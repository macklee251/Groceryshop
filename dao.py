# Data as object
from Models import *
import re

class DaoCategoria:
    @classmethod
    def salvarCategoria(cls, categoria:Categoria):
        with open('categorias.txt', 'a') as file:
            file.write(f'Nome: {categoria.nome}, Descrição: {categoria.descricao}\n')
            
    @classmethod
    def lerCategoria(cls):
        categorias = []
        with open('categorias.txt', 'r') as file:
            for line in file:
                match = re.search(r'Nome: (.*), Descrição: (.*)', line)
                if match:
                    nome = match.group(1)
                    descricao = match.group(2)
                    categorias.append(Categoria(nome, descricao))
        return categorias
    
class DaoProduto:
    @classmethod
    def salvarProduto(cls, produto:Produto):
        with open('produtos.txt', 'a') as file:
            file.write(f'Nome: {produto.nome}, Categoria: {produto.categoria}, Preço: {produto.preco}\n')
            
    @classmethod
    def lerProduto(cls):
        produtos = []
        with open('produtos.txt', 'r') as file:
            for line in file:
                match = re.search(r'Nome: (.*), Categoria: (.*), Preço: (.*)', line)
                if match:
                    nome = match.group(1)
                    categoria = match.group(2)
                    preco = match.group(3)
                    produtos.append(Produto(nome, categoria, preco))
        return produtos
        
class DaoEstoque:
    @classmethod
    def salvarEstoque(cls, estoque:Estoque):
        with open('estoque.txt', 'a') as file:
            file.write(f'Produto: {estoque.produto}, Quantidade: {estoque.quantidade}\n')
        
    @classmethod
    def lerEstoque(cls):
        estoques = []
        with open('estoque.txt', 'r') as file:
            for line in file:
                match = re.search(r'Produto: (.*), Quantidade: (.*)', line)
                if match:
                    produto = match.group(1)
                    quantidade = match.group(2)
                    estoques.append(Estoque(produto, quantidade))
        return estoques

class DaoVenda:
    @classmethod
    def salvarVenda(cls, venda:Venda):
        with open('vendas.txt', 'a') as file:
            file.write(f'Produto: {venda.produto}, Vendedor: {venda.vendedor}, Comprador: {venda.comprador}, Quantidade: {venda.quantidade}, Data: {venda.date}\n')
            
    @classmethod
    def lerVenda(cls):
        vendas = []
        with open('vendas.txt', 'r') as file:
            for line in file:
                match = re.search(r'Produto: (.*), Vendedor: (.*), Comprador: (.*), Quantidade: (.*), Data: (.*)', line)
                if match:
                    produto = match.group(1)
                    vendedor = match.group(2)
                    comprador = match.group(3)
                    quantidade = match.group(4)
                    date = match.group(5)
                    vendas.append(Venda(produto, vendedor, comprador, quantidade, date))
        return vendas
    
class DaoFornecedor:
    @classmethod
    def salvarFornecedor(cls, fornecedor:Fornecedor):
        with open('fornecedores.txt', 'a') as file:
            file.write(f'Nome: {fornecedor.nome}, CNPJ: {fornecedor.cnpj}, Telefone: {fornecedor.telefone}, Categoria: {fornecedor.categoria}\n')
            
    @classmethod
    def lerFornecedor(cls):
        fornecedores = []
        with open('fornecedores.txt', 'r') as file:
            for line in file:
                match = re.search(r'Nome: (.*), CNPJ: (.*), Telefone: (.*), Categoria: (.*)', line)
                if match:
                    nome = match.group(1)
                    cnpj = match.group(2)
                    telefone = match.group(3)
                    categoria = match.group(4)
                    fornecedores.append(Fornecedor(nome, cnpj, telefone, categoria))
        return fornecedores
    
class DaoPessoa:
    @classmethod
    def salvarPessoa(cls, pessoa:Pessoa):
        with open('pessoas.txt', 'a') as file:
            file.write(f'Nome: {pessoa.nome}, Telefone: {pessoa.telefone}, CPF: {pessoa.cpf}, Email: {pessoa.email}, Endereço: {pessoa.endereco}\n')
            
    @classmethod
    def lerPessoa(cls):
        pessoas = []
        with open('pessoas.txt', 'r') as file:
            for line in file:
                match = re.search(r'Nome: (.*), Telefone: (.*), CPF: (.*), Email: (.*), Endereço: (.*)', line)
                if match:
                    nome = match.group(1)
                    telefone = match.group(2)
                    cpf = match.group(3)
                    email = match.group(4)
                    endereco = match.group(5)
                    pessoas.append(Pessoa(nome, telefone, cpf, email, endereco))
        return pessoas
    
class DaoFunionario:
    @classmethod
    def salvarFuncionario(cls, funcionario:Funcionario):
        with open('funcionarios.txt', 'a') as file:
            file.write(f'Nome: {funcionario.nome}, CLT: {funcionario.clt}, Telefone: {funcionario.telefone}, CPF: {funcionario.cpf}, Email: {funcionario.email}, Endereço: {funcionario.endereco}\n')
            
    @classmethod
    def lerFuncionario(cls):
        funcionarios = []
        with open('funcionarios.txt', 'r') as file:
            for line in file:
                match = re.search(r'Nome: (.*), CLT: (.*), Telefone: (.*), CPF: (.*), Email: (.*), Endereço: (.*)', line)
                if match:
                    nome = match.group(1)
                    clt = match.group(2)
                    telefone = match.group(3)
                    cpf = match.group(4)
                    email = match.group(5)
                    endereco = match.group(6)
                    funcionarios.append(Funcionario(nome, clt, telefone, cpf, email, endereco))
        return funcionarios
    
if __name__=="__main__":
    DaoProduto().salvarProduto('Arroz', 'Alimento', '5.00')