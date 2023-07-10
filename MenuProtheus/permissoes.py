import win32security
import ntsecuritycon as con
import os
import ctypes
import time

os.system('cls')
def verifica_permissao(caminho_arquivo):
    # Obtém informações de segurança do arquivo
    info = win32security.GetFileSecurity(caminho_arquivo, win32security.DACL_SECURITY_INFORMATION)
    dacl = info.GetSecurityDescriptorDacl()
    
    # Verifica as permissões do usuário "Usuários"
    for i in range(dacl.GetAceCount()):
        ace = dacl.GetAce(i)
        sid = ace[-1]
        name, domain, type = win32security.LookupAccountSid(None, sid)
        if sid == win32security.ConvertStringSidToSid("S-1-5-32-545"):
            mask = ace[1]
           
            """print(f"Permissões do usuário {name}:")
            print(f"  Modificar: {bool(mask & con.FILE_GENERIC_WRITE)}")
            print(f"  Ler e Executar: {bool(mask & con.FILE_GENERIC_EXECUTE)}")
            print(f"  Ler: {bool(mask & con.FILE_GENERIC_READ)}")
            print(f"  Escrever: {bool(mask & con.FILE_WRITE_DATA)}")
            print(f"  Permissões especiais: {bool(mask & con.FILE_ALL_ACCESS)}") """
        
            # Verifica se todas as permissões estão presentes
            if (mask & con.FILE_GENERIC_WRITE) and (mask & con.FILE_GENERIC_EXECUTE) and (mask & con.FILE_GENERIC_READ) and (mask & con.FILE_WRITE_DATA) and (mask & con.FILE_ALL_ACCESS):
                return True
    return False

def altera_permissao(caminho_arquivo):
    # Obtém informações de segurança do arquivo
    info = win32security.GetFileSecurity(caminho_arquivo, win32security.DACL_SECURITY_INFORMATION)
    dacl = info.GetSecurityDescriptorDacl()
    
    # Adiciona permissões ao usuário "Usuários"
    sid = win32security.ConvertStringSidToSid("S-1-5-32-545")
    dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_GENERIC_WRITE | con.FILE_GENERIC_EXECUTE | con.FILE_GENERIC_READ | con.FILE_WRITE_DATA | con.FILE_ALL_ACCESS, sid)
    
    # Atualiza as informações de segurança do arquivo
    info.SetSecurityDescriptorDacl(1, dacl, 0)
    win32security.SetFileSecurity(caminho_arquivo, win32security.DACL_SECURITY_INFORMATION, info)

def main():
    caminho_arquivo = r"C:\Program Files\Protheus_2210\smartclient.ini"
    
    # Verifica se o arquivo possui as permissões solicitadas
    if not verifica_permissao(caminho_arquivo):
        # Verifica se o programa está sendo executado por um administrador
        if ctypes.windll.shell32.IsUserAnAdmin():
            altera_permissao(caminho_arquivo)
            print("\033[92mPermissões do arquivo alteradas com sucesso.\033[0m")
            time.sleep(3)
        else:
            print("\033[91mPara o correto funcionamento, favor primeiro executar o programa como administrador.\033[0m")
            time.sleep(3)

if __name__ == "__main__":
    main()
