# Data as object
from Models import *
import re

class DaoCategoria:
    @classmethod
    def salvar(cls, categoria:Categoria):
        with open('categorias.txt', 'a') as file:
            file.write(f'Nome: {categoria.nome}, Descrição: {categoria.descricao}\n')
            
    @classmethod
    def ler(cls):
        categorias = []
        with open('categorias.txt', 'r') as file:
            for line in file:
                match = re.search(r'Nome: (.*), Descrição: (.*)', line)
                if match:
                    nome = match.group(1)
                    descricao = match.group(2)
                    categorias.append(Categoria(nome, descricao))
        return categorias


class DaoVenda:
    @classmethod
    def salvar(cls, venda:Venda):
        with open('vendas.txt', 'a') as file:
            file.write(f'Produto: {venda.produto}, Vendedor: {venda.vendedor}, Comprador: {venda.comprador}, Quantidade: {venda.quantidade}, Data: {venda.date}\n')
            
    @classmethod
    def ler(cls):
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
    
    
if __name__=="__main__":
    print(DaoVenda().ler()[0])