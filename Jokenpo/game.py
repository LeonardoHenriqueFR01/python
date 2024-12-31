# JOKENPO em Python

from random import randint
from time import sleep


# Função para linhas no código
def Linhas():
    print('\033[32m-\033[m' * 70)   


# Função para título de regras
def Regras(txt):
    print(f'{f"{txt:>45}"}')


# Função para ganhos
def Ganho():
    print('\033[32m-=-\033[m' * 23)
    print(f'\033[4;32m{"VENCEU":^69}\033[m')
    print('\033[32m-=-\033[m' * 23)


# Função para perdas
def Perda():
    print('\033[31m-=-\033[m' * 23)
    print(f'\033[4;31m{"PERDEU":^69}\033[m')
    print('\033[31m-=-\033[m' * 23)


# Função para empates
def Empate():
    print('\033[33m-=-\033[m' * 23)
    print(f'\033[4;33m{"EMPATE":^69}\033[m')
    print('\033[33m-=-\033[m' * 23)


# Função para sair do game e mostrar os resulados
def Resul():
    print('[+] Finalizando...')
    sleep(3)
    Linhas()
    print(f'[+] Você ganhou {ganhos} vezes. \n[+] Perdeu {perdas} vezes. \n[+] Empatou {empates} vezes.')


print("""\033[35m
         ██╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗██████╗  ██████╗ 
         ██║██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║██╔══██╗██╔═══██╗
         ██║██║   ██║█████╔╝ █████╗  ██╔██╗ ██║██████╔╝██║   ██║
    ██   ██║██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║██╔═══╝ ██║   ██║
    ╚█████╔╝╚██████╔╝██║  ██╗███████╗██║ ╚████║██║     ╚██████╔╝
     ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                            \033[m""")
print(f'{"By leozindev_genius":>60} \n\033[33m{"v1.0.0":>55}\033[m')
Linhas()

# Regras
Regras('\033[33mREGRAS\033[m')
print('[+] Escolha a sua opção. \n[+] A maquina irá escolher. \n[+] Sua opção deve vencer a maquina de acordo com as regras de ganhos.')
Linhas()

# Variaveis de estatisticas
ganhos = perdas = empates = 0

# Biblioteca de jogadas
jogadas = {1:'PEDRA', 2:'PAPEL', 3:'TESOURA'}

# Loop infinito
while True:
    print(f'[+] \033[33mOpções de jogada\033[m {"[ 1 PEDRA] [ 2 PAPEL] [ 3 TESOURA]":>40}')
    Linhas()
    try:    
        jogada = int(input('[+] Escolha a sua jogada: ')) # Pegando a jogada do usuário
        
        if jogada < 1 or jogada > 3: # Caso o usuário não digite uma das opções
            print('\033[31mEscolha apenas 1, 2 ou 3! Tente novamente.\033[m')
            continue
    
    except ValueError: # Caso o usuário não digite um número inteiro valido
        print('\033[31mEscolha um número inteiro valido! Tente novamente.\033[m')
        continue

    except Exception as e: # Caso aconteça um erro inesperado
        print(e)
        continue
    
    # Mensagem com delay de maquina jogando...
    print('[+] Maquina jogando...')
    sleep(3)
    Linhas()

    maquina = randint(1, 3) # Para sortear um número entre 1 a 3 para a maquina

    # Todas as possiveis jogadas de ganhos
    if (jogada == 1 and maquina == 3) or (jogada == 2 and maquina == 1) or (jogada == 3 and maquina == 2):
        ganhos += 1 # Calcula 1 ganho

        # Mostrando as jogadas feitas pelo usuário e pela maquina
        print(f'[+] Você jogou {jogadas[jogada]}. \n[+] Maquina jogou {jogadas[maquina]}.')
        Linhas()
        Ganho()
        try:
            escolha = int(input('[+] [ 1 CONTINUAR] [ 0 VER ESTATISTICAS]: '))
            Linhas()
            if escolha == 1:
                continue
            
            elif escolha == 0:
                Resul()
                break
        
        except ValueError: # Caso o usuário não digite um número inteiro valido
            print('\033[31mDigite um número inteiro valido! Tente novamente.\033[m')
            continue

    # Caso o usuário escolha a mesma jogada que a maquina
    elif jogada == maquina:
        empates += 1 # Calcula mais 1 empate

        # Mostrando as jogadas feitas pelo usuário e pela maquina
        print(f'[+] Você jogou {jogadas[jogada]}. \n[+] Maquina jogou {jogadas[maquina]}.')
        Linhas()
        Empate()
        try:
            escolha = int(input('[+] [ 1 CONTINUAR] [ 0 VER ESTATISTICAS]: '))
            Linhas()
            if escolha == 1:
                continue
            
            elif escolha == 0:
                Resul()
                break
        
        except ValueError: # Caso o usuário não digite um número inteiro valido
            print('\033[31mDigite um número inteiro valido! Tente novamente.\033[m')
            continue

    # Caso nehuma opção acima aconteça ou seja o usuário perde
    else:
        perdas += 1 # Calcula mais 1 perda

        # Mostrando as jogadas feitas pelo usuário e pela maquina
        print(f'[+] Você jogou {jogadas[jogada]}. \n[+] Maquina jogou {jogadas[maquina]}.')
        Linhas()
        Perda()
        try:
            escolha = int(input('[+] [ 1 CONTINUAR] [ 0 VER ESTATISTICAS]: '))
            Linhas()
            if escolha == 1:
                continue
            
            elif escolha == 0:
                Resul()
                break
        
        except ValueError: # Caso o usuário não digite um número inteiro valido
            print('\033[31mDigite um número inteiro valido! Tente novamente.\033[m')
            continue
