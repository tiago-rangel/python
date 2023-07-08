import configparser
import sys
import os
import time

#Este trecho de código testa se o arquivo possui os atributos de escrita necessários para a execução do programa

file_path = "C:\\Program Files\\Protheus_2210\\smartclient.ini"

if os.access(file_path, os.W_OK):
    print("\033[32mPermissão para escrita\033[0m")
else:
    print("\033[31mPermissão de somente leitura. Deseja alterar a permissão do arquivo?\033[0m")
    user_input = input("Digite 's' para sim e 'n' para não: ")
    while user_input not in ['s', 'n']:
        print("\033[31mOpção inválida\033[0m")
        user_input = input("Digite 's' para sim e 'n' para não: ")
    if user_input == 's':
        os.chmod(file_path, 0o777)
    else:
        print("\033[31mO sistema será encerrado\033[0m")
        time.sleep(3)
        exit()
# Este trecho de código realiza a primeira leitura do arquivo

config = configparser.ConfigParser()
config.read("C:\Program Files\Protheus_2210\smartclient.ini")
os.system('cls')

#Descrição dos ambientes configurados, para exibir quando a opção [9] For selecionada.

ambientes = {
    ('10.14.115.12', '1111'): '[ 1 ] Padrão',
    ('10.14.115.12', '1240'): '[ 2 ] MyMobility',
    ('10.14.115.12', '1299'): '[ 3 ] MyMobility_1299',
    ('10.14.115.12', '1263'): '[ 4 ] Estoque',
    ('10.14.115.30', '1301'): '[ 5 ] Logística',
    ('10.14.115.30', '1302'): '[ 6 ] Oficina',
    ('10.14.115.30', '1303'): '[ 7 ] Safran Representações',
    ('10.14.115.12', '1304'): '[ 8 ] Ambiente de Validação'
}
server = config.get('tcp', 'server')
port = config.get('tcp', 'port')
ambiente = ambientes.get((server, port))
print("\n\033[34m" + f"Seu ambiente atual é: Ambiente {ambiente} server={server} e port={port}\n" + "\033[0m")

#Trecho responsável por exibir o menu de opções para o usuário, ler a opção escolhida e executar as funcionalidades atribuidas.

opcao = 0
while opcao != 10:
    print('Este é um configurador de ambiente para o sistema Protheus.\n\nEscolha uma das opções abaixo.\n')
    print("\033[34m" + ' _____________________________________________________________' + "\033[0m")
    print("\033[34m" + '''|                                                            |
|       [ 1 ] Padrão                                         |
|       [ 2 ] MyMobility                                     |
|       [ 3 ] MyMobility_1299                                |
|       [ 4 ] Estoque                                        |
|       [ 5 ] Logística                                      |
|       [ 6 ] Oficina                                        |
|       [ 7 ] Safran Representações                          |
|       [ 8 ] Ambiente de Validação                          |
|       [ 9 ] Verificar ambiente                             |
|       [ 10 ] Sair do configurador e Abrir o Protheus       |
|                                                            |''' + "\033[0m")
    print("\033[34m" + ' _____________________________________________________________' + "\033[0m")

   
    # Solicita ao usuário que digite a opção e testa é válida.

    while True:
      try:
          opcao = int(input('\nQual é a sua opção? '))
          if opcao not in range(1, 11):
              print('\033[91mOpção inválida. Tente novamente.\033[0m')
          else:
              break
      except ValueError:
          print('\033[91mEntrada inválida. Tente novamente.\033[0m')


    # De acordo com a opção escolhida pelo usuário é executada a alteração do campo TCP do arquivo ini

    if opcao == 1:
        os.system('cls')
        config.set('tcp', 'server', '10.14.115.12')
        config.set('tcp', 'port', '1111')
        with open('C:\Program Files\Protheus_2210\smartclient.ini', 'w') as configfile:
            config.write(configfile)
        server = config.get('tcp', 'server')
        port = config.get('tcp', 'port')
        ambiente = ambientes.get((server, port))
        print("\033[32m" + f"Reconfigurado para: Ambiente {ambiente} server={server} e port={port}\n"+ "\033[0m")

    elif opcao == 2:
        os.system('cls')
        config.set('tcp', 'server', '10.14.115.12')
        config.set('tcp', 'port', '1240')
        with open('C:\Program Files\Protheus_2210\smartclient.ini', 'w') as configfile:
            config.write(configfile)
        server = config.get('tcp', 'server')
        port = config.get('tcp', 'port')
        ambiente = ambientes.get((server, port))
        print("\033[32m" + f"Reconfigurado para: Ambiente {ambiente} server={server} e port={port}\n"+ "\033[0m")

    elif opcao == 3:
        os.system('cls')
        config.set('tcp', 'server', '10.14.115.12')
        config.set('tcp', 'port', '1299')
        with open('C:\Program Files\Protheus_2210\smartclient.ini', 'w') as configfile:
            config.write(configfile)
        server = config.get('tcp', 'server')
        port = config.get('tcp', 'port')
        ambiente = ambientes.get((server, port))
        print("\033[32m" + f"Reconfigurado para: Ambiente {ambiente} server={server} e port={port}\n"+ "\033[0m")

    elif opcao == 4:
        os.system('cls')
        config.set('tcp', 'server', '10.14.115.12')
        config.set('tcp', 'port', '1263')
        with open('C:\Program Files\Protheus_2210\smartclient.ini', 'w') as configfile:
            config.write(configfile)
        server = config.get('tcp', 'server')
        port = config.get('tcp', 'port')
        ambiente = ambientes.get((server, port))
        print("\033[32m" + f"Reconfigurado para: Ambiente {ambiente} server={server} e port={port}\n"+ "\033[0m")

    elif opcao == 5:
        os.system('cls')
        config.set('tcp', 'server', '10.14.115.30')
        config.set('tcp', 'port', '1301')
        with open('C:\Program Files\Protheus_2210\smartclient.ini', 'w') as configfile:
            config.write(configfile)
        server = config.get('tcp', 'server')
        port = config.get('tcp', 'port')
        ambiente = ambientes.get((server, port))
        print("\033[32m" + f"Reconfigurado para: Ambiente {ambiente} server={server} e port={port}\n"+ "\033[0m")

    elif opcao == 6:
        os.system('cls')
        config.set('tcp', 'server', '10.14.115.30')
        config.set('tcp', 'port', '1302')
        with open('C:\Program Files\Protheus_2210\smartclient.ini', 'w') as configfile:
            config.write(configfile)
        server = config.get('tcp', 'server')
        port = config.get('tcp', 'port')
        ambiente = ambientes.get((server, port))
        print("\033[32m" + f"Reconfigurado para: Ambiente {ambiente} server={server} e port={port}\n"+ "\033[0m")

    elif opcao == 7:
        os.system('cls')
        config.set('tcp', 'server', '10.14.115.30')
        config.set('tcp', 'port', '1303')
        with open('C:\Program Files\Protheus_2210\smartclient.ini', 'w') as configfile:
            config.write(configfile)
        server = config.get('tcp', 'server')
        port = config.get('tcp', 'port')
        ambiente = ambientes.get((server, port))
        print("\033[32m" + f"Reconfigurado para: Ambiente {ambiente} server={server} e port={port}\n"+ "\033[0m")

    elif opcao == 8:
        os.system('cls')
        config.set('tcp', 'server', '10.14.115.12')
        config.set('tcp', 'port', '1304')
        with open('C:\Program Files\Protheus_2210\smartclient.ini', 'w') as configfile:
            config.write(configfile)
        server = config.get('tcp', 'server')
        port = config.get('tcp', 'port')
        ambiente = ambientes.get((server, port))
        print("\033[32m" + f"Reconfigurado para: Ambiente {ambiente} server={server} e port={port}\n"+ "\033[0m")
        
    elif opcao ==9:
         os.system('cls')
         server = config.get('tcp', 'server')
         port = config.get('tcp', 'port')
         ambiente = ambientes.get((server, port))
         print("\033[34m" + f"Seu ambiente atual é: Ambiente {ambiente} server={server} e port={port}\n" + "\033[0m")

#Finaliza o programa e abre  o Protheus com a configuração escolhida.

os.system('cls')
import os
import sys

while True:
    try:
        opcao = input('\nDeseja abrir o Protheus? (s/n) ')
        if opcao == 's':
            os.system(r'"C:\Program Files\Protheus_2210\smartclient.exe"')
            sys.exit()
        elif opcao == 'n':
            break
        else:
            print('\033[91mOpção inválida. Tente novamente.\033[0m')
    except ValueError:
        print('\033[91mEntrada inválida. Tente novamente.\033[0m')