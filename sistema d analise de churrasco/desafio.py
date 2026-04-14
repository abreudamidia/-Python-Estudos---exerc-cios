from rich import print
from rich.panel import Panel


class Churrasco:
    consumo_padrao:float = 0.400 #Cada pessoa come em média 400g de carne
    preco_kg:float = 82.40 #Cada carne custa R$ 82.40

    def __init__(self,titulo,quant):
        #atributos de instancia
        self.titulo = titulo
        self.participantes = quant

    def __str__(self):
        return f'Esse é {self.titulo} com {self.participantes} pessoas participando.'

    def calcular_qtd_carne(self) -> float:
        return self.participantes * self.consumo_padrao

    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * self.__class__.preco_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.participantes

    def analisar(self):
        conteudo = f'Analisando [green] {self.titulo}[/] com [blue] {self.participantes} convidados [/].'
        conteudo += f'\n Cada participante comerá {Churrasco.consumo_padrao} Kg e cada Kg custa R$ {Churrasco.preco_kg:,.2f}'
        conteudo += f'\n Recomendo comprar {self.calcular_qtd_carne():.3f} de carne'
        conteudo += f'\n O custo total será de [green]R${self.calcular_custo_total():,.2f}[/]'
        conteudo += f'\n cada pessoa pagará [yellow]R${self.calcular_custo_individual():,.2f}[/] para participar'
        painel = Panel(conteudo, title=self.titulo)
        print(painel)


c1 = Churrasco("Churras dos Amigos",15)
c1.analisar()
c2 = Churrasco("Festa da firma",90)
c2.analisar()

