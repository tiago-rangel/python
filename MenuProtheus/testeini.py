import configparser
config = configparser.ConfigParser()
config.read("C:\Program Files\Protheus_2210\smartclient.ini")
print (config.sections())

for section in config.sections():
    print(f'Seção: {section}')
    for key in config[section]:
        print(f'{key} = {config[section][key]}')