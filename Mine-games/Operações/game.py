from random import randint
from time import sleep

# Função para linhas no código
def Linhas():
    print('\033[32m-\033[m' * 45)



# Função para fazer as operações
def Opera_easy():
    print('[+] Entrando no modo EASY...')
    sleep(3)
    while True:
        n1 = randint(1, 10)
        n2 = randint(1, 10)
        n3 = randint(1, 10)
        soma = n1 // n2 * n3 - n2
        try:
            print('[+] Resolva a soma abaixo:')
            resposta = int(input(f'[+] {n1} // {n2} * {n3} - {n2} = '))
            if resposta == soma:
                print(f'[+] \033[32mParabêns você acertou! A resposta era {soma} \033[m')
                
                escolha = int(input('[ 0 EXIT MODE ] [ 1 CONTINUE ]: '))
                if escolha == 0:
                    print('[+] Finalizando modo EASY...')
                    sleep(3)
                    break
                
                elif escolha == 1:
                    continue

            else:
                print('[+] \033[31mErrou tente novamente.\033[m')
                continue
        
        except ValueError:
            print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
            continue


# Exibe o cabeçalho do programa
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

while True:
    try:
        modo = int(input('[+] \033[31m[ 0 EXIT ]\033[m [ 1 EASY ] [ 2 MEDIUM] [ 3 HARD ]: '))
        if modo == 0:
            print('[+] Finalizando programa...')  
            sleep(3)
            break

        elif modo < 1 or modo > 3:
            print('[+] \033[31mEscolha apenas 0, 1, 2 ou 3! Tente novamente.\033[m')
            continue

        elif modo == 1:
            Opera_easy()
        
    except ValueError:
        print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
        continue
