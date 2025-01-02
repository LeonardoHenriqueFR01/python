# Par ou Impar com Python

from time import sleep
from random import randint


# Função para linhas no código
def Linhas():
    print('\033[32m-\033[m' * 90)


# Função de mensagem para ganhos
def Ganho():
    print('\033[32m-=-\033[m' * 30)
    print(f'\033[32m{"VENCEU":^90}\033[m')
    print('\033[32m-=-\033[m' * 30)


# Função de mensagens para perdas
def Perda():
    print('\033[31m-=-\033[m' * 30)
    print(f'\033[31m{"PERDEU":^90}\033[m')
    print('\033[31m-=-\033[m' * 30)


# Função para continuar o game ou mostrar as estatisticas
def Estact_():
    while True: # Loop infinito
        try:
            opcao = int(input('[+] [ 1 CONTINUAR ] [ 2 ESTATISTICAS ] Escolha a sua opção: ')) # Pegando a opção do usuário
            Linhas()
            
            if opcao < 1 or opcao > 2: # Caso o usuário não escolha 1 nem 2
                print('[+] \033[31mEscolha apenas 1 ou 2! Tente novamente.\033[m')
                continue

        except ValueError: # Caso o usuário não digite um número inteiro valido
            print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')

        except Exception as e: # Caso aconteça um erro inesperado
            print(e)

        if opcao == 1: # Continua o game
            break
                   
        elif opcao == 2: # Mostra as estatisticas de game e continua o game
            print(f'[+] Total de ganhos: {ganhos}. \n[+] Total de perdas: {perdas}.')
            Linhas()
            break


# Função para mostrar o resultado quando for um número Par
def Resul_Par():
    print(f'[+] Seu número é {num}. \n[+] É o número da maquina é {maquina} \n[+] A soma dos número são {soma} Dando um número PAR.')
    Linhas()


# Função para mostrar o resultado quando for um número Impar
def Resul_Impar():
    print(f'[+] Seu número é {num}. \n[+] É o número da maquina é {maquina} \n[+] A soma dos número são {soma} Dando um número IMPAR.')
    Linhas()


print("""\033[35m
██████╗  █████╗ ██████╗      ██████╗ ██████╗     ██╗███╗   ███╗██████╗  █████╗ ██████╗ 
██╔══██╗██╔══██╗██╔══██╗    ██╔═══██╗██╔══██╗    ██║████╗ ████║██╔══██╗██╔══██╗██╔══██╗
██████╔╝███████║██████╔╝    ██║   ██║██████╔╝    ██║██╔████╔██║██████╔╝███████║██████╔╝
██╔═══╝ ██╔══██║██╔══██╗    ██║   ██║██╔══██╗    ██║██║╚██╔╝██║██╔═══╝ ██╔══██║██╔══██╗
██║     ██║  ██║██║  ██║    ╚██████╔╝██║  ██║    ██║██║ ╚═╝ ██║██║     ██║  ██║██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝    ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝
                                                                                       \033[m""")
print(f'{"By leozindev_genius":>90} \n\033[33m{"v1.0.0":>85}\033[m')
print('[+] \033[31mDigite 0 para sair.\033[m')
Linhas()

# Regras do game
print(f'{"REGRAS":^85}')
print('[+] Escolha um número qualquer. \n[+] Escolha PAR ou IMPAR. \n[+] A maquina irá escolher um número. \n[+] A soma dos números deve ser a opção que você escolheu.')
Linhas()


# Variaveis de estatisticas
ganhos = perdas = 0

while True: # Loop infinito
    try:
        # Pegando o número escolhido pelo usuário
        num = int(input('[+] Escolha um número inteiro: '))

        if num == 0:
            print('Finalizando...')
            sleep(3)
            break 

    except ValueError: # Caso o usuário não digite um número inteiro valido
        print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
        continue

    except Exception as e: # Caso aconteça um erro inesperado
        print(e)
    
    while True: 
        try:
            escolha = int(input('[+] [ 1 PAR ] [ 2 IMPAR ] Escolha a sua opção: ')) # Pegando a opção do usuário Par ou Impar
            Linhas()  

            if escolha < 1 or escolha > 2: # Caso o usuário não escolha a opção 1 nem a 2
                print('\033[31mDigite apenas 1 ou 2! Tente novamente.\033[m')
                continue

        except ValueError: # Caso o usuário não digite um número inteiro valido
            print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
            continue 

        except Exception as e: # Caso aconteça um erro inesperado
            print(e)


        maquina = randint(1, 100) # Pegando um número de 1 a 100 para a maquina
        soma = num + maquina # Somando o número do usuário + o da maquina


        if soma % 2 == 0 and escolha == 1: # Usuário ganha com resultado de PAR
            ganhos += 1 # Pega todos os ganhos
            Ganho() # Mostra uma mensagem de ganho
            Resul_Par() # Mostra o resultado da rodada
            Estact_() # Mostra as estatisticas de game e continua o game
            break # Para o Loop e volta o game do início

        elif soma % 2 == 1 and escolha == 2: # Usuário ganha com resultado de IMPAR
            ganhos += 1
            Ganho()
            Resul_Impar()
            Estact_()
            break

        elif soma % 2 == 0 and escolha == 2: # Usuário perde com resultado de PAR
            perdas += 1
            Perda()
            Resul_Par()
            Estact_()
            break

        elif soma % 2 == 1 and escolha == 1: # Usuário perde com resultado de IMPAR
            perdas += 1
            Perda()
            Resul_Impar()
            Estact_()
            break
