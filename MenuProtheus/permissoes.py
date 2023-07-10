import os
import ctypes
import sys
import time
import win32security
import ntsecuritycon as con

def verifica_permissao(caminho_arquivo):
    # Obtém informações de segurança do arquivo
    info = win32security.GetFileSecurity(caminho_arquivo, win32security.DACL_SECURITY_INFORMATION)
    dacl = info.GetSecurityDescriptorDacl()
    
    # Verifica se o arquivo possui as permissões necessárias
    for i in range(dacl.GetAceCount()):
        ace = dacl.GetAce(i)
        if ace[1] == con.FILE_GENERIC_READ | con.FILE_GENERIC_WRITE | con.FILE_GENERIC_EXECUTE | con.FILE_ALL_ACCESS:
            return True
    return False

def verifica_admin():
    try:
        # Verifica se o programa está sendo executado como administrador
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def altera_permissao(caminho_arquivo):
    try:
        # Altera as permissões do arquivo para permitir leitura, escrita, execução e permissões especiais
        info = win32security.GetFileSecurity(caminho_arquivo, win32security.DACL_SECURITY_INFORMATION)
        dacl = info.GetSecurityDescriptorDacl()
        dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_GENERIC_READ | con.FILE_GENERIC_WRITE | con.FILE_GENERIC_EXECUTE | con.FILE_ALL_ACCESS, win32security.ConvertStringSidToSid("S-1-1-0"))
        info.SetSecurityDescriptorDacl(1, dacl, 0)
        win32security.SetFileSecurity(caminho_arquivo, win32security.DACL_SECURITY_INFORMATION, info)
        return True
    except:
        return False

def main():
    caminho_arquivo = r"C:\Program Files\Protheus_2210\smartclient.ini"
    
    if verifica_permissao(caminho_arquivo):
        print("O arquivo já possui as permissões necessárias.")
    else:
        if verifica_admin():
            if altera_permissao(caminho_arquivo):
                print("\033[32mPermissões do arquivo alteradas com sucesso.\033[0m")
                time.sleep(3)
            else:
                print("\033[31mErro ao alterar as permissões do arquivo.\033[0m")
                time.sleep(3)
        else:
            print("\033[31mPara o correto funcionamento, favor primeiro executar o programa como administrador.\033[0m")
            time.sleep(3)
            sys.exit()

if __name__ == "__main__":
    main()
caminho_arquivo = r"C:\Program Files\Protheus_2210\smartclient.ini"
print(verifica_permissao(caminho_arquivo))
