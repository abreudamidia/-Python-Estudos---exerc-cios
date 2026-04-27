#Declaração de Classe
class Gafanhoto:

    def __init__(self):  #Metodo construtor
        #Atributos de Instancia
        self.nome = ""
        self.idade = 0

     #Método de Instância
    def aniversario(self):
        self.idade +=1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade."


#Declaração de Objetos
g1 = Gafanhoto()
g1.nome = "Danilo"
g1.idade = 23
g1.aniversario()
print(g1.mensagem())
