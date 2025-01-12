from random import randint
from time import sleep


# Função para linhas
def Linhas():
    print('\033[32m-\033[m' * 50)


# Função para título das opções
def Text(txt):
    Linhas()
    print(f'\033[4;33m{f"{txt:^50}"}\033[m')
    Linhas()


# Função para fazer somas
def Soma():
    Text('SOMA')
    while True:
        print('[+] \033[32m[ 2 VALORES ] [ 3 VALORES ] [ 4 VALORES ]\033[m \033[31m[ 0 SAIR ]\033[m')
        try:
            count_valor = int(input('[+] Escolha a quantidade de valores: '))
            
            if count_valor == 0:
                print('[+] Saindo do modo SOMA...')
                sleep(3)
                break

            elif count_valor < 2 or count_valor > 4:
                print('[+] \033[31mEscolha apenas 2, 3, ou 4! Tente novamente.\033[m')

            if count_valor == 2:
                n1 = randint(1, 1000)
                n2 = randint(1, 1000)
                soma = n1 + n2

                while True:
                    try:
                        resposta = int(input(f'[+] Responda: {n1} + {n2} = '))

                        if resposta == soma:
                            print(f'[+] Você acertou {n1} + {n2} = {soma}')
                            break
                        else:
                            print('[+] \033[31mErrou! Tente novamente.\033[m')
                            continue
                    except ValueError:
                        print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
                        continue
            
            elif count_valor == 3:
                n1 = randint(1, 1000)
                n2 = randint(1, 1000)
                n3 = randint(1, 1000)
                soma = n1 + n2 + n3

                while True:
                    try:
                        resposta = int(input(f'[+] Responda: {n1} + {n2} + {n3} = '))

                        if resposta == soma:
                            print(f'[+] Você acertou {n1} + {n2} + {n3} = {soma}')
                            break
                        else:
                            print('[+] \033[31mErrou! Tente novamente.\033[m')
                            continue
                    except ValueError:
                        print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
                        continue

            elif count_valor == 4:
                n1 = randint(1, 1000)
                n2 = randint(1, 1000)
                n3 = randint(1, 1000)
                n4 = randint(1, 1000)
                soma = n1 + n2 + n3 + n4

                while True:
                    try:
                        resposta = int(input(f'[+] Responda: {n1} + {n2} + {n3} + {n4} = '))

                        if resposta == soma:
                            print(f'[+] Você acertou {n1} + {n2} + {n3} + {n4} = {soma}')
                            break
                        else:
                            print('[+] \033[31mErrou! Tente novamente.\033[m')
                            continue
                    except ValueError:
                        print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
                        continue


        except ValueError:
            print('[+]\033[31m Digite um número inteiro valido! Tente novamente.\033[m')

print("""\033[34m
     ██████╗ ██████╗ ███████╗██████╗  █████╗ 
    ██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗
    ██║   ██║██████╔╝█████╗  ██████╔╝███████║
    ██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗██╔══██║
    ╚██████╔╝██║     ███████╗██║  ██║██║  ██║
     ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
                                         \033[m""")
print(f'{"By Leozindev_genius":>45}')
Linhas()

print('\033[31m[ 0 SAIR ]\033[m \n\033[34m[ 1 SOMA ] [ 2 ADCIÇÃO ] [ 3 MULTIPLICAÇÃO ] \n[ 4 POTENCIA ] [ 5 TODOS ++ ]\033[m')
Linhas()
while True:
    try:
        opção = int(input('[+] Escolha a sua opção: '))
        
        if opção == 0:
            print('[+] Finalizando programa...')
            sleep(3)
            break

        elif opção < 1 or opção > 5:
            print('[+] \033[31mEscolha apenas 1, 2, 3, 4, 5 ou 0 para sair! Tente novamente.\033[m')
            continue
        
        if opção == 1:
            Soma()

    except ValueError:
        print('\033[31mDigite um número inteiro valido! Tente novamente.\033[m')
        continue

