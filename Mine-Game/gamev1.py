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


# Função pra título dos games
def Title_game(txt):
    print('[+] Entrando no game...')
    sleep(3) 
    Linhas()
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


# Função para tocar a musica do game
def Music():
    pygame.mixer.init()
    pygame.mixer.music.load('/home/leonardo/Downloads/music-game.mp3')
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


Music()
print("""  \033[34m[ 1 JOKENPOL] / [ 2 IMPAR / PAR]\033[m / \033[32m[ 3 LOTERIA ] / [ 4 ACERTE O NÚMERO ]\033[m""") # Jogos disponiveis
Linhas()
while True:
    try:    
        game = int(input('[+] Escolha o que vai jogar: '))
    except ValueError:
        print('\033[31mEscolha um número inteiro valido! Tente novamente.\033[m')
        continue
    
    if game == 1:
        Title_game('JOKENPOL')
