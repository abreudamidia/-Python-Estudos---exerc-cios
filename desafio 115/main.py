
from desafios.uteis.utilidades import cabecalho
from desafios.uteis.fun_cod import menu,cadastrados,cadastrar
from desafios.uteis.validacoes import leia_int
from desafios.arquivos.meusarquivos import *

arq = 'curso em vídeo.txt'
if not arquivoexiste(arq):
    criararquivo(arq)


while True:
    cabecalho("MENU PRINCIPAL".center(50))
    menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"])
    opcao = leia_int("Sua Opção: ")
    if opcao == 1:
        lerarquivo(arq)
    elif opcao == 2:
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leia_int("Idade: ")
        cadastrar(arq, nome, idade)
    elif opcao == 3:
        print(f"Saindo do sistema...Até Logo!".center(50))
        break
    else:
        print(f"\033[33mERRO! Digite Uma opção válida!\033[m")


