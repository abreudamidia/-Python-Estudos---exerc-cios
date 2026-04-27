#Declaração de Classe
class Gafanhoto:

    def __init__(self,n = '', i = 0):  #Metodo construtor
        #Atributos de Instancia
        self.nome = n
        self.idade = i

     #Método de Instância
    def aniversario(self):
        self.idade +=1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade."

    def __getstate__(self):
        return f"EEstado: nome = {self.nome} ; idade = {self.idade}"


#Declaração de Objetos
g1 = Gafanhoto('maria',17)
g1.aniversario()
print(g1.mensagem())
print(g1.__getstate__())

g2 = Gafanhoto('Marcos',35)
g2.aniversario()
print(g2.mensagem())

g3 = Gafanhoto('Vazio',)
print(g3.mensagem())
