import configparser
config = configparser.ConfigParser()

#Adiciona novos dados ao arquivo

config.set('tcp', 'server', '10.14.115.13')
config.set('tcp', 'port', '1122')

with open('C:\Program Files\Protheus_2210\smartclient.ini', 'w') as configfile:
    config.write(configfile)


"""
print('Este é um configurador de ambiente para o sistema Protheus. \n')
print('Escolha uma das opções abaixo. \n')
print('''[ 1 ] Padrão
[ 2 ] MyMobility
[ 3 ] MyMobility_1299
[ 4 ] Estoque
[ 5 ] Logística
[ 6 ] Oficina
[ 7 ] Safran Representações
[ 8 ] Ambiente de Validação
[ 9 ] Sair do configurador''')
#opcao = str(input('Qual é a sua opção? '))
"""