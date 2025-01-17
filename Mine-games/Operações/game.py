from random import randint  # Importação para gerar números aleatórios
from time import sleep  # Importação para criar pausas no programa

# Função para exibir linhas decorativas
def Linhas():
    print('\033[32m-\033[m' * 55)


# Função para fazer operações no modo EASY
def Opera_easy():
    print('[+] Entrando no modo EASY...')
    sleep(3)  # Pausa para simular carregamento
    erros = acertos = 0  # Inicialização de contadores
    while True:
        # Geração de números aleatórios para a operação
        n1 = randint(1, 10)
        n2 = randint(1, 10)
        n3 = randint(1, 10)
        soma = n1 // n2 * n3 - n2  # Cálculo da expressão
        try:
            print('[+] Resolva a soma abaixo:')
            resposta = int(input(f'[+] {n1} // {n2} * {n3} - {n2} = '))  # Entrada do usuário
            
            if resposta == soma:  # Verificação da resposta
                print(f'[+] \033[32mParabéns você acertou! A resposta era {soma} \033[m')
                acertos += 1  # Incremento de acertos
                
                # Opção para continuar ou sair
                escolha = int(input('[ 0 EXIT MODE ] [ 1 CONTINUE ]: '))
                if escolha == 0:  # Finalizar modo
                    print('[+] Finalizando modo EASY...')
                    sleep(3)
                    print(f'[+] Você teve um total de {acertos} acertos.\n[+] E um total de {erros} erros.')
                    sleep(3)
                    break
                elif escolha == 1:
                    continue  # Continuar no modo
                else:
                    print('[+] \033[31mOpção inválida! Tente novamente.\033[m')
            else:
                print('[+] \033[31mErrou tente novamente.\033[m')  # Mensagem de erro
                erros += 1
        except ValueError:
            print('[+] \033[31mDigite um número inteiro válido! Tente novamente.\033[m')  # Tratamento de erro para entrada inválida


# Função para fazer operações no modo MEDIUM
def Opera_medium():
    print('[+] Entrando no modo MEDIUM...')
    sleep(3)
    erros = acertos = 0
    while True:
        # Geração de números aleatórios
        n1 = randint(1, 10)
        n2 = randint(1, 10)
        n3 = randint(1, 10)
        n4 = randint(1, 10)
        n5 = randint(1, 10)
        soma = n1 // n2 * (n3 - n2) % n4 + n5  # Cálculo da expressão
        try:
            print('[+] Resolva a soma abaixo:')
            resposta = int(input(f'[+] {n1} // {n2} * ({n3} - {n2}) % {n4} + {n5} = '))
            
            if resposta == soma:
                print(f'[+] \033[32mParabéns você acertou! A resposta era {soma} \033[m')
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
                    print('[+] \033[31mOpção inválida! Tente novamente.\033[m')
            else:
                print('[+] \033[31mErrou tente novamente.\033[m')
                erros += 1
        except ValueError:
            print('[+] \033[31mDigite um número inteiro válido! Tente novamente.\033[m')


# Função para fazer operações no modo HARD
def Opera_hard():
    print('[+] Entrando no modo HARD...')
    sleep(3)
    erros = acertos = 0
    while True:
        # Geração de números aleatórios
        n1 = randint(1, 10)
        n2 = randint(1, 10)
        n3 = randint(1, 10)
        n4 = randint(1, 10)
        n5 = randint(1, 10)
        n6 = randint(1, 10)
        n7 = randint(1, 10)
        n8 = randint(1, 10)
        soma = n1 // n2 * (n3 - n2) % (n4 + n5) ** n6 // n7 + n8  # Cálculo complexo
        try:
            print('[+] Resolva a soma abaixo:')
            resposta = int(input(f'[+] {n1} // {n2} * ({n3} - {n2}) % ({n4} + {n5}) ** {n6} // {n7} + {n8} = '))
            
            if resposta == soma:
                print(f'[+] \033[32mParabéns você acertou! A resposta era {soma} \033[m')
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
                    print('[+] \033[31mOpção inválida! Tente novamente.\033[m')
            else:
                print('[+] \033[31mErrou tente novamente.\033[m')
                erros += 1
        except ValueError:
            print('[+] \033[31mDigite um número inteiro válido! Tente novamente.\033[m')


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

# Loop principal para selecionar modos
while True:
    try:
        modo = int(input('[+] \033[31m[ 0 EXIT ] \033[32m[ 1 EASY ] \033[33m[ 2 MEDIUM] \033[31m[ 3 HARD ]\033[m: '))
        if modo == 0:  # Sair do programa
            print('[+] Finalizando programa...')
            sleep(3)
            break
        elif modo == 1:
            Opera_easy()  # Chama o modo EASY
        elif modo == 2:
            Opera_medium()  # Chama o modo MEDIUM
        elif modo == 3:
            Opera_hard()  # Chama o modo HARD
        else:
            print('[+] \033[31mEscolha apenas 0, 1, 2 ou 3! Tente novamente.\033[m')
    except ValueError:
        print('[+] \033[31mDigite um número inteiro válido! Tente novamente.\033[m')
