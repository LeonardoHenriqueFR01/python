# Par ou Impar com Python

from time import sleep
from random import randint


# Função para linhas no código
def Linhas():
    print('\033[32m-\033[m' * 90)


# Função para ganhos
def Ganho():
    print('\033[32m-=-\033[m' * 23)
    print(f'\033[32m{"VENCEU":^69}\033[m')
    print('\033[32m-=-\033[m' * 23)


# Função para perdas
def Perda():
    print('\033[31m-=-\033[m' * 23)
    print(f'\033[4;31m{"PERDEU":^69}\033[m')
    print('\033[31m-=-\033[m' * 23)



# Função para mostrar o resultado quando for um número Par
def Resul_Par():
    print(f'[+] Seu número é {num}. \n[+] É o número da maquina é {maquina} \n[+] A soma dos número são {soma} Dando um número PAR.')


# Função para mostrar o resultado quando for um número Impar
def Resul_Impar():
    print(f'[+] Seu número é {num}. \n[+] É o número da maquina é {maquina} \n[+] A soma dos número são {soma} Dando um número IMPAR.')


print("""\033[35m
██████╗  █████╗ ██████╗      ██████╗ ██████╗     ██╗███╗   ███╗██████╗  █████╗ ██████╗ 
██╔══██╗██╔══██╗██╔══██╗    ██╔═══██╗██╔══██╗    ██║████╗ ████║██╔══██╗██╔══██╗██╔══██╗
██████╔╝███████║██████╔╝    ██║   ██║██████╔╝    ██║██╔████╔██║██████╔╝███████║██████╔╝
██╔═══╝ ██╔══██║██╔══██╗    ██║   ██║██╔══██╗    ██║██║╚██╔╝██║██╔═══╝ ██╔══██║██╔══██╗
██║     ██║  ██║██║  ██║    ╚██████╔╝██║  ██║    ██║██║ ╚═╝ ██║██║     ██║  ██║██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝    ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝
                                                                                       \033[m""")
print(f'{"By leozindev_genius":>90} \n\033[33m{"v1.0.0":>85}\033[m')
Linhas()

# Regras do game
print(f'{"REGRAS":^85}')
print('[+] Escolha um número qualquer. \n[+] Escolha PAR ou IMPAR. \n[+] A maquina irá escolher um número. \n[+] A soma dos números deve ser a opção que você escolheu.')
Linhas()

while True: # Loop infinito
    try:
        # Pegando o número escolhido pelo usuário
        num = int(input('[+] Escolha um número inteiro: '))

        while True: 
            try:
                escolha = int(input('[+] [ 1 PAR ] [ 2 IMPAR ] Escolha a sua opção: ')) # Pegando a opção do usuário Par ou Impar
                Linhas()  
                
                if escolha == True:
                    break

                elif escolha < 1 or escolha > 2: # Caso o usuário não escolha a opção Impar nem a Par
                    print('[+] \033[31mEscolha 1 ou 2! Tente novamente.\033[m')
                    continue

            except ValueError: # Caso o usuário não digite um número inteiro valido
                print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
                continue 
    
    except ValueError: # Caso o usuário não digite um número inteiro valido
        print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
        continue

    # Variaveis de estatisticas
    ganhos = perdas = 0

    maquina = randint(1, 100) # Pegando um número de 1 a 100 para a maquina
    soma = num + maquina # Somando o número do usuário + o da maquina


    if soma % 2 == 0 and escolha == 1:
        Ganho()
        Resul_Par()

    elif soma % 2 == 1 and escolha == 2:
        Ganho()
        Resul_Impar()
    
    elif soma % 2 == 0 and escolha == 2:
        Perda()
        Resul_Par()

    elif soma % 2 == 1 and escolha == 1:
        Perda()
        Resul_Impar()
