import configparser
config = configparser.ConfigParser()
config.read("C:\Program Files\Protheus_2210\smartclient.ini")

secao = 'tcp'
chave = 'server'
porta = 'port'

ip = config.get(secao, chave)
porta = config.get(secao, porta)
print("O servidor é: {}\nPorta: {}".format(ip, porta))

# Apaga toda a section do arquivo

"""
config.remove_section('tcp')
f =open('C:\Program Files\Protheus_2210\smartclient.ini', 'w')
config.write(f)
f.close()
"""

# Adiciona novos dados ao arquivo

config.set('tcp', 'server', '10.14.115.12')
config.set('tcp', 'port', '1111')

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


"""
#Adiciona novos dados ao arquivo

config.set('tcp', 'server', '10.14.115.12')
config.set('tcp', 'port', '1111')
with open('C:\Program Files\Protheus_2210\smartclient.ini', 'w') as configfile:
    config.write(configfile)

"""


"""
Informações

1 - Padrão

server=10.14.115.12
port=1111


2 - MyMobility

server=10.14.115.12
port=1240

3 - MyMobility_1299

server=10.14.115.12
port=1299

4 - Estoque

server=10.14.115.12
port=1263

5 - Logística

server=10.14.115.30
port=1301

6 - Oficina

server=10.14.115.30
port=1302

7 - Representações

server=10.14.115.12
port=1262

8 - Validação

server=10.14.115.31
port=1456

"""
