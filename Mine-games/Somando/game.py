from random import randint  # Importa a função randint para gerar números aleatórios
from time import sleep  # Importa a função sleep para criar atrasos na execução


# Função para imprimir uma linha decorativa
def Linhas():
    print('\033[32m-\033[m' * 50)


# Função para exibir o título com formatação
def Text(txt):
    Linhas()  # Imprime uma linha decorativa antes do título
    print(f'\033[4;33m{f"{txt:^50}"}\033[m')  # Exibe o título centralizado e com formatação
    Linhas()  # Imprime uma linha decorativa após o título


# Função para realizar operações de soma
def Soma():
    Text('SOMA')  # Exibe o título "SOMA"
    while True:
        # Exibe as opções disponíveis para o usuário
        print('[+] \033[32m[ 2 VALORES ] [ 3 VALORES ] [ 4 VALORES ]\033[m \033[31m[ 0 SAIR ]\033[m') 
        try:
            count_valor = int(input('[+] Escolha a quantidade de valores: '))  # Solicita a quantidade de valores

            if count_valor == 0:  # Verifica se o usuário escolheu sair
                print('[+] Saindo do modo SOMA...')
                sleep(3)  # Aguarda 3 segundos antes de sair
                break

            elif count_valor < 2 or count_valor > 4:  # Verifica se a escolha é inválida
                print('[+] \033[31mEscolha apenas 2, 3, ou 4! Tente novamente.\033[m')

            if count_valor == 2:  # Caso o usuário escolha somar 2 valores
                n1 = randint(1, 1000)  # Gera um número aleatório entre 1 e 1000
                n2 = randint(1, 1000)
                soma = n1 + n2  # Calcula a soma dos números

                while True:
                    try:
                        resposta = int(input(f'[+] Responda: {n1} + {n2} = '))  # Solicita a resposta do usuário

                        if resposta == soma:  # Verifica se a resposta está correta
                            print(f'[+] Você acertou {n1} + {n2} = {soma}')
                            break
                        else:  # Caso a resposta esteja errada
                            print('[+] \033[31mErrou! Tente novamente.\033[m')
                            continue
                    except ValueError:  # Trata entradas inválidas que não sejam números inteiros
                        print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
                        continue
            
            elif count_valor == 3:  # Caso o usuário escolha somar 3 valores
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

            elif count_valor == 4:  # Caso o usuário escolha somar 4 valores
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

        except ValueError:  # Trata erros de entrada de dados
            print('[+]\033[31m Digite um número inteiro valido! Tente novamente.\033[m')

# Função para multiplicação
def Multiplica():
    # Exibe um título formatado para o modo MULTIPLICAÇÃO
    Text('MULTIPLICAÇÃO')
    while True:
        # Exibe as opções de quantidade de valores para multiplicação
        print('[+] \033[32m[ 2 VALORES ] [ 3 VALORES ] [ 4 VALORES ]\033[m \033[31m[ 0 SAIR ]\033[m')
        try:
            # Solicita ao usuário a escolha da quantidade de valores para multiplicação
            count_valor = int(input('[+] Escolha a quantidade de valores: '))
            
            # Caso o usuário escolha 0, o programa sai do modo MULTIPLICAÇÃO
            if count_valor == 0:
                print('[+] Saindo do modo MULTIPLICAÇÃO...')
                sleep(3)
                break

            # Valida se a escolha é inválida (não está entre 2 e 4)
            elif count_valor < 2 or count_valor > 4:
                print('[+] \033[31mEscolha apenas 2, 3, ou 4! Tente novamente.\033[m')

            # Multiplicação de dois valores
            if count_valor == 2:
                n1 = randint(1, 1000)  # Gera um número aleatório entre 1 e 1000
                n2 = randint(1, 1000)
                soma = n1 * n2  # Realiza a multiplicação dos dois números

                while True:
                    try:
                        # Solicita ao usuário que insira o resultado da multiplicação
                        resposta = int(input(f'[+] Responda: {n1} x {n2} = '))

                        # Verifica se a resposta está correta
                        if resposta == soma:
                            print(f'[+] Você acertou {n1} x {n2} = {soma}')
                            break
                        else:
                            print('[+] \033[31mErrou! Tente novamente.\033[m')
                            continue
                    except ValueError:
                        # Caso o usuário insira um valor inválido
                        print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
                        continue

            # Multiplicação de três valores
            elif count_valor == 3:
                n1 = randint(1, 1000)
                n2 = randint(1, 1000)
                n3 = randint(1, 1000)
                soma = n1 * n2 * n3  # Multiplica os três números gerados

                while True:
                    try:
                        # Solicita ao usuário que insira o resultado da multiplicação
                        resposta = int(input(f'[+] Responda: {n1} x {n2} x {n3} = '))

                        # Verifica se a resposta está correta
                        if resposta == soma:
                            print(f'[+] Você acertou {n1} x {n2} x {n3} = {soma}')
                            break
                        else:
                            print('[+] \033[31mErrou! Tente novamente.\033[m')
                            continue
                    except ValueError:
                        # Caso o usuário insira um valor inválido
                        print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
                        continue

            # Multiplicação de quatro valores
            elif count_valor == 4:
                n1 = randint(1, 1000)
                n2 = randint(1, 1000)
                n3 = randint(1, 1000)
                n4 = randint(1, 1000)
                soma = n1 * n2 * n3 * n4  # Multiplica os quatro números gerados

                while True:
                    try:
                        # Solicita ao usuário que insira o resultado da multiplicação
                        resposta = int(input(f'[+] Responda: {n1} x {n2} x {n3} x {n4} = '))

                        # Verifica se a resposta está correta
                        if resposta == soma:
                            print(f'[+] Você acertou {n1} x {n2} x {n3} x {n4} = {soma}')
                            break
                        else:
                            print('[+] \033[31mErrou! Tente novamente.\033[m')
                            continue
                    except ValueError:
                        # Caso o usuário insira um valor inválido
                        print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
                        continue

        except ValueError:
            # Mensagem para entrada inválida na escolha da quantidade de valores
            print('[+]\033[31m Digite um número inteiro valido! Tente novamente.\033[m')


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
    # Exibe o menu principal
    print('\033[31m[ 0 SAIR ]\033[m \n\033[34m[ 1 SOMA ] [ 2 ADCIÇÃO ] [ 3 MULTIPLICAÇÃO ] \n[ 4 POTENCIA ] [ 5 TODOS ++ ]\033[m')
    Linhas()
    try:
        opção = int(input('[+] Escolha a sua opção: '))  # Solicita a escolha do usuário

        if opção == 0:  # Finaliza o programa
            print('[+] Finalizando programa...')
            sleep(3)
            break

        elif opção < 1 or opção > 5:  # Validações para entradas fora do intervalo esperado
            print('[+] \033[31mEscolha apenas 1, 2, 3, 4, 5 ou 0 para sair! Tente novamente.\033[m')
            continue

        if opção == 1:
            Soma()  # Chama a função Soma

        elif opção == 2:
            Multiplica()  # Chama a função Multiplica

    except ValueError:  # Trata entradas inválidas
        print('\033[31mDigite um número inteiro valido! Tente novamente.\033[m')
        continue
