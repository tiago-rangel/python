import ctypes
import win32security
import ntsecuritycon as con
import configparser
import sys
import time
import os

# O trecho abaixo verifica se o Protheus está devidamente instalado no computador.
os.system('cls')

if not os.path.exists(r'C:\Program Files\Protheus_2210\smartclient.ini'):
    print('\033[31m' + 'O Protheus não está corretamente instalado neste computador' + '\033[0m')
    time.sleep(4)
    sys.exit()
    
# trecho que limpa a tela e é informado o caminho do arquivo para verificação
os.system('cls')

arquivo = "C:\\Program Files\\Protheus_2210\\smartclient.ini"

# Verificando se o programa está sendo executado por um usuário com privilégios de administrador
if ctypes.windll.shell32.IsUserAnAdmin():
    # Obtendo o SID dos usuários locais
    sid = win32security.ConvertStringSidToSid("S-1-5-32-545")

    # Obtendo as informações de segurança do arquivo
    sd = win32security.GetFileSecurity(arquivo, win32security.DACL_SECURITY_INFORMATION)

    # Obtendo a DACL atual do arquivo
    dacl = sd.GetSecurityDescriptorDacl()

    # Verificando se os usuários já possuem as permissões solicitadas
    users_permissoes = False

    for i in range(dacl.GetAceCount()):
        ace = dacl.GetAce(i)
        if ace[2] == sid:
            users_permissoes = True

    if not users_permissoes:
        # Adicionando os usuários com permissão de controle total
        dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, sid)

        # Atualizando as informações de segurança do arquivo
        sd.SetSecurityDescriptorDacl(1, dacl, 0)
        win32security.SetFileSecurity(arquivo, win32security.DACL_SECURITY_INFORMATION, sd)

        # Exibindo a mensagem na cor verde utilizando ANSI
        print("\033[32mPermissões do arquivo alteradas\033[0m")
        time.sleep(3)
else:
    # Exibindo a mensagem na cor vermelha utilizando ANSI
    print("\033[31mFavor executar com uma conta de administrador para realizar as devidas configurações.\033[0m")

    # Pausando a execução do programa por 3 segundos
    time.sleep(3)
    
    # Encerrando o programa
    sys.exit()

os.system('cls')

# Este trecho de código realiza novamente a leitura do arquivo para executar as tarefas de alteração conforme a opção do menu

file_path = "C:\\Program Files\\Protheus_2210\\smartclient.ini"
config = configparser.ConfigParser()
config.read(file_path)

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
while opcao != 10 :
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
        with open(file_path, 'w') as configfile:
            config.write(configfile)
        server = config.get('tcp', 'server')
        port = config.get('tcp', 'port')
        ambiente = ambientes.get((server, port))
        print("\033[32m" + f"Reconfigurado para: Ambiente {ambiente} server={server} e port={port}\n" + "\033[0m")

    if opcao == 2:
        os.system('cls')
        config.set('tcp', 'server', '10.14.115.12')
        config.set('tcp', 'port', '1240')
        with open(file_path, 'w') as configfile:
            config.write(configfile)
        server = config.get('tcp', 'server')
        port = config.get('tcp', 'port')
        ambiente = ambientes.get((server, port))
        print("\033[32m" + f"Reconfigurado para: Ambiente {ambiente} server={server} e port={port}\n" + "\033[0m")

    if opcao == 3:
        os.system('cls')
        config.set('tcp', 'server', '10.14.115.12')
        config.set('tcp', 'port', '1299')
        with open(file_path, 'w') as configfile:
            config.write(configfile)
        server = config.get('tcp', 'server')
        port = config.get('tcp', 'port')
        ambiente = ambientes.get((server, port))
        print("\033[32m" + f"Reconfigurado para: Ambiente {ambiente} server={server} e port={port}\n" + "\033[0m")

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
        
        #Programa desemvolvido por Tiago Ribeiro Rangel