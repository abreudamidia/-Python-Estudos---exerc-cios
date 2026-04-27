from uteis import traco
from rich import print
class ContaBancaria:
    """Cria uma conta bancária e permite fazer saques e depósitos"""

    def __init__(self,id,nome = 'Desconhecido',saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"[green]Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:,.2f}")


    def __str__(self):
        return f":book: [yellow]A conta {self.id}, do titular, {self.titular} tem saldo {self.saldo:.2f}"

    def depositar (self,valor):
        self.saldo += valor
        traco()
        print(f"[blue]Depósito de {valor} autorizado na conta {self.id}")
        print(f":money_with_wings: Novo saldo de : {self.saldo}")
        traco()


    def sacar (self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
            traco()
            print(f"[red]Saque de {valor} autorizado na conta {self.id}")
            print(f":money_with_wings: Novo saldo de : {self.saldo}")
            traco()
        else:
            traco()
            print(f":money_with_wings: Saldo não disponível:")
            print(f"Você tentou sacar {valor},mais seu saldo é de {self.saldo}.\nSaindo!" )
            traco()







c1 = ContaBancaria(112,"Gustavo",2600)
c1.depositar(345)
c1.sacar(1220)
print(str(c1))
