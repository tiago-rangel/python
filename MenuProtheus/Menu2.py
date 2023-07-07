import os
import configparser
config = configparser.ConfigParser()
config.read("C:\Program Files\Protheus_2210\smartclient.ini")
os.system('cls')
print(
    f"Seu ambiente atual é server={config.get('tcp', 'server')} e port={config.get('tcp', 'port')}")
opcao = 0
while opcao != 9:
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
    [ 9 ] Sair do configurador\n''')
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
os.system('cls')
print('Fim da execução')

#if not opcao.isdigit() or int(opcao) not in range(1, 10):