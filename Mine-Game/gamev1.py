# Mine Game em Python

from time import sleep
import random as rd
import pygame
import os

# Para tirar mensagens especificas
os.environ['PYDEVD_DISABLE_FILE_VALIDATION'] = '1'


# Função para colocar linhas no código
def Linhas():
    print('\033[34m-\033[m' * 75)


# Função para entrada dos games
def Entrada_game(txt):
    print('[+] Entrando no game...')
    sleep(3) 
    Linhas()
    if game == 1: # Para cada game irá tocar uma música diferente 
        Music_game1()
    elif game == 2:
        Music_game2()
    elif game == 3:
        Music_game3()
    elif game == 4:
        Music_game4()
    print('\033[33m-=-\033[m' * 25)
    print(f'\033[4;35m{f"{txt}":^75}\033[m')
    print('\033[33m-=-\033[m' * 25)


# Função para ganhos
def Ganho():
    print('\033[32m-=-\033[m' * 15)
    print(f'\033[4;32m{"VENCEU":^45}\033[m')
    print('\033[32m-=-\033[m' * 15)


# Função para perdas
def Perda():
    print('\033[31m-=-\033[m' * 15)
    print(f'\033[4;31m{"PERDEU":^45}\033[m')
    print('\033[31m-=-\033[m' * 15)


# Função para perdas
def Empate():
    print('\033[33m-=-\033[m' * 15)
    print(f'\033[4;33m{"EMPATE":^45}\033[m')
    print('\033[33m-=-\033[m' * 15)


# Função para tocar a musica principal
def Music():
    pygame.mixer.init()
    pygame.mixer.music.load('/home/leonardo/Downloads/music-game.mp3')
    pygame.mixer.music.play()
    

# Função para tocar musica de game 1
def Music_game1():
    pygame.mixer.init()
    pygame.mixer.music.load('/home/leonardo/Downloads/music-game01.mp3')
    pygame.mixer.music.play()


# Função para tocar musica de game 2
def Music_game2():
    pygame.mixer.init()
    pygame.mixer.music.load('/home/leonardo/Downloads/music-game02.mp3')
    pygame.mixer.music.play()


# Função para tocar musica de game 3
def Music_game3():
    pygame.mixer.init()
    pygame.mixer.music.load('/home/leonardo/Downloads/music-game03.mp3')
    pygame.mixer.music.play()


# Função para tocar musica de game 4
def Music_game4():
    pygame.mixer.init()
    pygame.mixer.music.load('/home/leonardo/Downloads/music-game04.mp3')
    pygame.mixer.music.play()


print("""\033[35m
███╗   ███╗██╗███╗   ██╗███████╗     ██████╗  █████╗ ███╗   ███╗███████╗
████╗ ████║██║████╗  ██║██╔════╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██╔████╔██║██║██╔██╗ ██║█████╗      ██║  ███╗███████║██╔████╔██║█████╗  
██║╚██╔╝██║██║██║╚██╗██║██╔══╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
██║ ╚═╝ ██║██║██║ ╚████║███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                                                        \033[m""")
print(f'{"By Leozindev_genius":>75} \n\033[33m{"v1.0.0":>70}\033[m')
Linhas()

# Para tocar a música principal
Music()

# Jogos disponiveis
print("""  \033[34m[ 1 JOKENPOL] / [ 2 IMPAR / PAR]\033[m / \033[32m[ 3 LOTERIA ] / [ 4 ACERTE O NÚMERO ]\033[m \n  \033[31m[ 0 SAIR ]\033[m""")
Linhas()

while True: # Loop infinito
    try:    
        game = int(input('[+] Escolha o que vai jogar: '))

    except ValueError: # Caso o usuário não digite um número inteiro valido
        print('\033[31mEscolha um número inteiro valido! Tente novamente.\033[m')
        continue

    except Exception as e: # Para erros inesperados
        print(e)
        continue

    if game == 0: # Para finalizar o game
        print('Finalizando...')
        sleep(3)
        break
    
    elif game == 1: # Para entrar no modo JOKENPOL
        Entrada_game('JOKENPOL')

    elif game == 2: # Para entrar no modo IMPAR / PAR
        Entrada_game('IMPAR / PAR')

    elif game == 3: # Para entrar no modo LOTERIA
        Entrada_game('LOTERIA')
    
    elif game == 4: # Para entrar no modo ACERTE O NÚMERO
        Entrada_game('ACERTE O NÚMERO')

    else: # Caso o usuário digite uma opção que não seja nenhuma das anteriores
        print('\033[31mOpção invalida! Tente novamente.\033[m')
        continue
