def menu(lista):
    for c, item in enumerate(lista, 1):
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[m")
    print('-' * 50)

def cadastrados():
    return 'Opção 1'.center(50)

def cadastrar(arquivo, name ='desconhecido',ida=0):
    try:
        a = open(arquivo, 'at')
    except:
        print("Falha ao abrir arquivo")
    else:
        try:
            a.write(f'{name};{ida}\n')
        except:
            print("ERRO! Ao escrever os dados")
        else:
            print(f"Novo registro de {name} adicionado com sucesso!")
            a.close()