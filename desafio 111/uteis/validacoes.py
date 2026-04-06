def leia_int(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print(f"\033[31mERRO! Por favor,digite um número inteiro valido!\033[m")
            continue
        except (KeyboardInterrupt):
            print(f"\nEntrada de dados interrompida!")
            return 0
        else:
            return num

def leia_float(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print(f"\033[31mERRO! Por Favor, Digite um número real valido!\033[m")
            continue
        except (KeyboardInterrupt):
            print(f"\nEntrada de dados interrompida!")
            return 0
        else:
            return num