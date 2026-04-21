from rich import print
from rich.table import Table

class Produto:
    def __init__(self, nome, preco_compra,preco_venda):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda

    def lucro(self):
        lucrototal = self.preco_venda - self.preco_compra
        return lucrototal


estoque = []
while True:
    p =  str(input("Nome do produto: "))
    pc = float(input("Preço de compra: "))
    pv = float(input("Preço de venda: "))

    estoque.append(Produto(p,pc,pv))
    while True:
        continuar = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
        if continuar in "SN":
            break
        else:
            print('INVÁLIDO!TENTE NOVAMENTE COM S ou N')
    if continuar == "N":
        break

tabela = Table(title="PRODUTOS VENDIDOS")
tabela.add_column("Produto",style="bold green")
tabela.add_column("Valor de compra:",style="bold green")
tabela.add_column("Valor de venda:",style="bold green")
tabela.add_column("Lucro Total: ",style="bold green")

for p in estoque:
    tabela.add_row(p.nome,str(p.preco_compra),str(p.preco_venda),str(p.lucro()))

print(tabela)