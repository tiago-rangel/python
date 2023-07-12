import os
import shutil
import subprocess
import time

os.system('cls')

def listar_diretorios():
    diretorios = []
    for letra in ['C', 'D', 'E']:
        if os.path.exists(f'{letra}:\\'):
            for nome in os.listdir(f'{letra}:\\'):
                if nome.lower().startswith('protheus') or nome.lower().startswith('smartclient') or nome.lower().startswith('smarclient'):
                    diretorios.append(f'{letra}:\\{nome}')
    return diretorios

def deletar_diretorios(diretorios):
    for diretorio in diretorios:
        if 'smartclient.exe' in os.listdir(diretorio):
            shutil.rmtree(diretorio)

def uninstall_protheus():
    # Crie uma lista para armazenar as informações de desinstalação
    protheus_versions = []
    
    # Defina a lista de pastas para verificar
    protheus_folders = [
        r'C:\Program Files\Protheus_33',
        r'C:\Program Files\Protheus_33_Mobility',
        r'C:\Program Files\Protheus_33_Validacao',
        r'C:\Program Files\Smarclient_33_Representacoes',
        r'C:\Program Files\Protheus_33_Oficina',
        r'C:\Program Files\Protheus_33_Logistica',
        r'C:\Program Files\Protheus_33_Estoque'
    ]
    
    # Verifique cada pasta para encontrar o desinstalador unins000.exe
    for protheus_folder in protheus_folders:
        if os.path.exists(protheus_folder):
            uninstaller_path = os.path.join(protheus_folder, 'unins000.exe')
            if os.path.exists(uninstaller_path):
                protheus_versions.append((os.path.basename(protheus_folder), uninstaller_path))
    
    # Adicione as pastas encontradas em C:, D: e E: à lista de versões do Protheus
    diretorios = listar_diretorios()
    for diretorio in diretorios:
        protheus_versions.append((os.path.basename(diretorio), None))
    
    if len(protheus_versions) > 0:
        # Imprima a lista de versões do Protheus encontradas
        print('\n\033[91m' + 'Versões do Protheus encontradas:\n')
        for name, _ in protheus_versions:
            print(name)
        print('\033[0m')
        
        # Pergunte ao usuário se deseja desinstalar as versões encontradas
        print('\033[92m' + '\nDeseja desinstalar s ou n?')
        answer = input()
        
        while answer not in ["s", "S", "n", "N"]:
            print("\033[31mOpção inválida!!! Digite 's' ou 'n'\033[0m")
            answer = input()
        
        print('\033[0m')
        
        if answer.lower() == 's':
            # Desinstale cada versão do Protheus encontrada
            for name, uninstall_string in protheus_versions:
                if uninstall_string is not None:
                    print(f'Desinstalando {name}...')
                    subprocess.call(f'"{uninstall_string}" /SILENT')
                    print(f'{name} desinstalado com sucesso.')
            
            # Verifique se as pastas foram excluídas e, se não, tente excluí-las
            for protheus_folder in protheus_folders:
                if os.path.exists(protheus_folder):
                    try:
                        shutil.rmtree(protheus_folder)
                        print(f'Pasta {protheus_folder} excluída com sucesso.')
                    except OSError:
                        print(f'Não foi possível excluir a pasta {protheus_folder}.')
            
            # Exclua todos os atalhos na área de trabalho do usuário, na área de trabalho pública e na pasta OneDrive que começam com "Protheus" ou "Smartclient"
            desktop_folders = [
                os.path.join(os.environ['USERPROFILE'], 'Desktop'),
                os.path.join(os.environ['PUBLIC'], 'Desktop'),
                os.path.join(os.environ['USERPROFILE'], 'OneDrive', 'Desktop')
            ]
            for desktop_folder in desktop_folders:
                if os.path.exists(desktop_folder):
                    for file in os.listdir(desktop_folder):
                        if file.startswith('Protheus') or file.startswith('Smartclient'):
                            try:
                                os.remove(os.path.join(desktop_folder, file))
                                print(f'Atalho {file} excluído com sucesso.')
                            except OSError:
                                print(f'Não foi possível excluir o atalho {file}.')
            
            # Exclua as pastas encontradas em C:, D: e E:
            deletar_diretorios(diretorios)
            
            # Limpe a tela e exiba uma mensagem de conclusão
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\033[92m' + 'Desinstalação concluída\033[0m')
            time.sleep(4)
        
        # Limpe a tela e encerre a execução
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print('\033[92m' + 'Nenhuma versão do Protheus 33 foi encontrada\033[0m')
        time.sleep(3)

uninstall_protheus()
