from random import randint
from time import sleep

# Função para linhas no código
def Linhas():
    print('\033[32m-\033[m' * 55)


# Função para fazer as operações modo EASY
def Opera_easy():
    print('[+] Entrando no modo EASY...')
    sleep(3)
    erros = acertos = 0
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
                acertos += 1
                
                escolha = int(input('[ 0 EXIT MODE ] [ 1 CONTINUE ]: '))
                if escolha == 0:
                    print('[+] Finalizando modo EASY...')
                    sleep(3)
                    print(f'[+] Você teve um total de {acertos} acertos.\n[+] E um total de {erros} erros.')
                    sleep(3)
                    break
                
                elif escolha == 1:
                    continue
                
                else:
                    print('[+] \033[31mOpção invalida! Tente novamente.\033[m')
                    continue
            
            else:
                print('[+] \033[31mErrou tente novamente.\033[m')
                erros += 1 
                continue
        
        except ValueError:
            print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
            continue


# Função para fazer as operações modo MEDIUM
def Opera_medium():
    print('[+] Entrando no modo MEDIUM...')
    sleep(3)
    erros = acertos = 0
    while True:
        n1 = randint(1, 10)
        n2 = randint(1, 10)
        n3 = randint(1, 10)
        n4 = randint(1, 10)
        n5 = randint(1, 10)

        soma = n1 // n2 * (n3 - n2) % n4 + n5
        try:
            print('[+] Resolva a soma abaixo:')
            resposta = int(input(f'[+] {n1} // {n2} * ({n3} - {n2}) % {n4} + {n5} = '))
            
            if resposta == soma:
                print(f'[+] \033[32mParabêns você acertou! A resposta era {soma} \033[m')
                acertos += 1

                escolha = int(input('[ 0 EXIT MODE ] [ 1 CONTINUE ]: '))
                if escolha == 0:
                    print('[+] Finalizando modo MEDIUM...')
                    sleep(3)
                    print(f'[+] Você teve um total de {acertos} acertos. \n[+] E um total de {erros} erros.')
                    sleep(3)
                    break
                
                elif escolha == 1:
                    continue
                
                else:
                    print('[+] \033[31mOpção invalida! Tente novamente.\033[m')
                    continue
            
            else:
                print('[+] \033[31mErrou tente novamente.\033[m')
                erros += 1
                continue
        
        except ValueError:
            print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
            continue


# Função para fazer as operações modo HARD
def Opera_hard():
    print('[+] Entrando no modo HARD...')
    sleep(3)
    erros = acertos = 0
    while True:
        n1 = randint(1, 10)
        n2 = randint(1, 10)
        n3 = randint(1, 10)
        n4 = randint(1, 10)
        n5 = randint(1, 10)
        n6 = randint(1, 10)
        n7 = randint(1, 10)
        n8 = randint(1, 10)        

        soma = n1 // n2 * (n3 - n2) % (n4 + n5) ** n6 // n7 + n8
        try:
            print('[+] Resolva a soma abaixo:')
            resposta = int(input(f'[+] {n1} // {n2} * ({n3} - {n2}) % ({n4} + {n5}) ** {n6} // {n7} + {n8} = '))
            
            if resposta == soma:
                print(f'[+] \033[32mParabêns você acertou! A resposta era {soma} \033[m')
                acertos += 1

                escolha = int(input('[ 0 EXIT MODE ] [ 1 CONTINUE ]: '))
                if escolha == 0:
                    print('[+] Finalizando modo HARD...')
                    sleep(3)
                    print(f'[+] Você teve um total de {acertos} acertos. \n[+] E um total de {erros} erros.')
                    sleep(3)
                    break
                
                elif escolha == 1:
                    continue
                
                else:
                    print('[+] \033[31mOpção invalida! Tente novamente.\033[m')
                    continue
            
            else:
                print('[+] \033[31mErrou tente novamente.\033[m')
                erros += 1
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
print(f'{"By Leozindev_genius":>55}')
Linhas()

while True:
    try:
        modo = int(input('[+] \033[31m[ 0 EXIT ] \033[32m[ 1 EASY ] \033[33m[ 2 MEDIUM] \033[31m[ 3 HARD ]\033[m: '))
        if modo == 0:
            print('[+] Finalizando programa...')  
            sleep(3)
            break

        elif modo < 1 or modo > 3:
            print('[+] \033[31mEscolha apenas 0, 1, 2 ou 3! Tente novamente.\033[m')
            continue

        elif modo == 1:
            Opera_easy()

        elif modo == 2:
            Opera_medium()

        elif modo == 3:
            Opera_hard()

    except ValueError:
        print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
        continue
