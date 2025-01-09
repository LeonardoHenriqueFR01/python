from twilio.rest import Client
from time import sleep
import pywhatkit as kit
from datetime import datetime, timedelta



# Credenciais do Twilio (obtidas na sua conta do Twilio)
account_sid = ''
auth_token = ''

# Crie o client Twilio
client = Client(account_sid, auth_token)


# Função para Linhas no código
def Linhas():
    print('\033[32m-\033[m' * 90)


# Função para fazer chamada
def Enviar_chamada():
    numero_destino = str(input('[+] Digite o número de destino: ')) # Pega o número que irá receber a chamada
    print('Processando...')
    sleep(2)

    # Cria a chamada
    call = client.calls.creat(
        to=numero_destino, # Número de destino
        from_='', # Número gerado pelo Twilio
        twiml='<Response><Say voice="alice" language="pt-BR">Bem-vindo ao sistema! Obrigado por testar o Twilio.</Say></Response>'
    )
    print(f'[+] Ligação iniciada com SID: {call.sid}')
    sleep(5)


# Função para enviar SMS
def Enviar_sms():
    numero_destino = str(input('[+] Digite o número de destino: '))
    mensagem = str(input('[+] Digite a mensagem a ser enviada: '))
    print('Processando...')
    sleep(2)

    try:
        # Envia o SMS para o número de destino
        message = client.messagens.create(
            body=mensagem, # Corpo da mensagem
            from_='', # Número gerado pelo Twilio
            to=numero_destino # Número para onde o SMS será enviado
        )
        print(f'[+] Mensagem enviada: {message.sid}')
        sleep(5)
    except Exception as e:
        print(f'[+] Erro ao enviar a mensagem: {e}')


# Função para enviar mensagem no Whatssapp
def Enviar_whatsapp():
    try:
        # Lista de números de destino com o código do pais (+55)
        numero_detino = ['']

        # Mensagem promocional a ser enviada
        mensagem = ''

        # Horario atual (adiciona um pequeno atraso para abir o Whatsapp Web)
        horario_atual = datetime.now() + timedelta(minuto=2) # Atrasando para garantir tempo suficiente
        hora = horario_atual.hour
        minuto = horario_atual.minute

        # Enviar a mensagem para cada número na lista
        for numero_destino in numero_destino:
            print(f'[+] Enviando mensagem para {numero_destino} ás {hora}:{minuto}...')

            # Envia a mensagem para o número
            kit.send2hatmsg(
                numero_destino, # Número de destino
                mensagem, # Mensagem de texto
                hora, # Hora para enviar
                minuto # Minuto do envio
            )

            print(f'[+] Mensagem enviada automaticamente para {numero_destino}!')
    
    except Exception as e:
        print(f'Erro ao enviar a mensagem {e}')

print("""\033[31m
     ▒█████  ▓█████  ██▓       ▓█████▄  ██▓  ██████  ██▓███   ▄▄▄       ██▀███   ▒█████  
    ▒██▒  ██▒▓█   ▀ ▓██▒       ▒██▀ ██▌▓██▒▒██    ▒ ▓██░  ██▒▒████▄    ▓██ ▒ ██▒▒██▒  ██▒
    ▒██░  ██▒▒███   ▒██░       ░██   █▌▒██▒░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██ ░▄█ ▒▒██░  ██▒
    ▒██   ██░▒▓█  ▄ ▒██░       ░▓█▄   ▌░██░  ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██▀▀█▄  ▒██   ██░
    ░ ████▓▒░░▒████▒░██████▒   ░▒████▓ ░██░▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒░██▓ ▒██▒░ ████▓▒░
    ░ ▒░▒░▒░ ░░ ▒░ ░░ ▒░▓  ░    ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▒░▒░▒░ 
    ░ ▒ ▒░  ░ ░  ░░ ░ ▒  ░    ░ ▒  ▒  ▒ ░░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░  ░▒ ░ ▒░  ░ ▒ ▒░ 
    ░ ░ ░ ▒     ░     ░ ░       ░ ░  ░  ▒ ░░  ░  ░  ░░         ░   ▒     ░░   ░ ░ ░ ░ ▒  
        ░ ░     ░  ░    ░  ░      ░     ░        ░                 ░  ░   ░         ░ ░  
                                ░                                                        \033[m""")
print('\033[33mV1.0.0\033[m', end='')
print(f'{"By Leozindev_genius":>85}')
Linhas()
print('[1] \033[33mFAZER CHAMADA\033[m [2] \033[33mENVIAR SMS\033[m [3] \033[33mENVIAR MENSAGEM WHATSAPP\033[m \n\033[31m[0] SAIR\033[m')
Linhas()

while True:
    try:
        opção = int(input('[+] Escolha uma das opções: '))

        if opção == 0:
            print('Finalizando programa...')
            sleep(2)
            break

        elif opção < 1 or opção > 3:
            print('[+] \033[31mEscolha apenas 1, 2, 3 ou 0\033[m')
            continue

        elif opção == 1:
            Enviar_chamada()
        
        elif opção == 2:
            Enviar_sms()
        
        elif opção == 3:
            Enviar_whatsapp()
    
    except ValueError:
        print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
        continue
