from rich import print
from rich.table import Table

class Clientes:
    def __init__(self, nome,plano,vencimento):
        self.nome = nome
        self.plano = plano
        self.vencimento = vencimento

meus_clientes = []

while True:
    nome_cliente = str(input("Nome do cliente: "))
    plano_cliente = int(input("Plano do cliente: "))
    vencimento_cliente = int(input("Quantos dias até o vencimento? : "))

    meus_clientes.append(Clientes(nome_cliente,plano_cliente,vencimento_cliente))
    while True:
        continuar = str(input("Deseja continuar? [s/n] ")).strip().upper()[0]
        if continuar in  "NS":
            break
        else:
            print(f"Tente novamente com S ou N")
    if continuar == "N":
        break

tabela = Table(title='ClIENTES TELEFLIX')
tabela.add_column("Nome:")
tabela.add_column("Vencimento:")
tabela.add_column("Custo:")

for cliente in meus_clientes:
    tabela.add_row(cliente.nome, str(cliente.plano), str(cliente.vencimento))
print()

print(tabela)

