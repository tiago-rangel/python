import configparser
config = configparser.ConfigParser()
config.read("C:\Program Files\Protheus_2210\smartclient.ini")

config.set('tcp', 'server', '10.14.115.30')
config.set('tcp', 'port', '1111')

with open('C:\Program Files\Protheus_2210\smartclient.ini', 'w') as configfile:
    config.write(configfile)
