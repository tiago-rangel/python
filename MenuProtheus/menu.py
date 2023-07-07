import os
import configparser

#Trecho responsável por ler as configurações do arquivo atuais

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
print(f"Seu ambiente atual é: Ambiente {ambiente} server={server} e port={port}\n")

#Trecho responsável por exibir o menu de opções para o usuário, ler a opção escolhida e executar as funcionalidades atribuidas.

opcao = 0
while opcao != 10:
    print('Este é um configurador de ambiente para o sistema Protheus.\nEscolha uma das opções abaixo.\n')
    print('**********************************************************')
    print('''
    [ 1 ] Padrão
    [ 2 ] MyMobility 
    [ 3 ] MyMobility_1299
    [ 4 ] Estoque
    [ 5 ] Logística
    [ 6 ] Oficina
    [ 7 ] Safran Representações
    [ 8 ] Ambiente de Validação
    [ 9 ] Verificar ambiente
    [ 10 ] Sair do configurador e Abrir o Protheus\n''')
    print('**********************************************************\n')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        config.set('tcp', 'server', '10.14.115.12')
        config.set('tcp', 'port', '1111')
        with open('C:\Program Files\Protheus_2210\smartclient.ini', 'w') as configfile:
            config.write(configfile)
    elif opcao == 2:
        config.set('tcp', 'server', '10.14.115.12')
        config.set('tcp', 'port', '1240')
        with open('C:\Program Files\Protheus_2210\smartclient.ini', 'w') as configfile:
            config.write(configfile)
    elif opcao == 3:
        config.set('tcp', 'server', '10.14.115.12')
        config.set('tcp', 'port', '1299')
        with open('C:\Program Files\Protheus_2210\smartclient.ini', 'w') as configfile:
            config.write(configfile)
    elif opcao == 4:
        config.set('tcp', 'server', '10.14.115.12')
        config.set('tcp', 'port', '1263')
        with open('C:\Program Files\Protheus_2210\smartclient.ini', 'w') as configfile:
            config.write(configfile)
    elif opcao == 5:
        config.set('tcp', 'server', '10.14.115.30')
        config.set('tcp', 'port', '1301')
        with open('C:\Program Files\Protheus_2210\smartclient.ini', 'w') as configfile:
            config.write(configfile)
    elif opcao == 6:
        config.set('tcp', 'server', '10.14.115.30')
        config.set('tcp', 'port', '1302')
        with open('C:\Program Files\Protheus_2210\smartclient.ini', 'w') as configfile:
            config.write(configfile)
    elif opcao == 7:
        config.set('tcp', 'server', '10.14.115.12')
        config.set('tcp', 'port', '1262')
        with open('C:\Program Files\Protheus_2210\smartclient.ini', 'w') as configfile:
            config.write(configfile)
    elif opcao == 8:
        config.set('tcp', 'server', '10.14.115.31')
        config.set('tcp', 'port', '1456')
        with open('C:\Program Files\Protheus_2210\smartclient.ini', 'w') as configfile:
            config.write(configfile)
    elif opcao ==9:
         server = config.get('tcp', 'server')
         port = config.get('tcp', 'port')
         ambiente = ambientes.get((server, port))
         print(f"Seu ambiente atual é: Ambiente {ambiente} server={server} e port={port}\n")

#Finaliza o programa e abre  o Protheus com a configuração escolhida.

os.system('cls')
if input("Deseja abrir o Protheus? (s/n) ") == "s":
    os.system(r'"C:\Program Files\Protheus_2210\smartclient.exe"')
