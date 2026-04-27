from rich import print

class Livro:
    def __init__(self, titulo, quantidade):
        self.titulo = titulo
        self.quantidade = quantidade
        self.pagina_atual = 1

        print(f':books:[blue]Você acabou de abrir o livro [red]{self.titulo}[/] que tem [green]{self.quantidade} páginas [/] no total. Você agora está na [yellow]página {self.pagina_atual}[/]')
    def avancar_paginas(self,tot):

        destino = self.pagina_atual + tot


        if self.limite():
            for c in range(self.pagina_atual,self.pagina_atual+tot):
                print(f'pág{self.pagina_atual+1} :arrow_forward: ',end = '')
                self.pagina_atual +=1
                paginas_restante = self.quantidade - self.pagina_atual
            print(f'[blue]Você avançou {tot} páginas e agora está na [yellow]página {self.pagina_atual}[/]')
        else:
            print(f"Você chegou ao fim do livro [red]{self.titulo}[/]")

    def limite(self):
        if self.pagina_atual <= self.quantidade:
            return True
        else:
            return False







l1 = Livro('10 coisas que aprendi',20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(20)