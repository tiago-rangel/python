import win32security
import ntsecuritycon as con

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
            print(f"Permissões do usuário {name}:")
            print(f"  Ler: {bool(mask & con.FILE_READ_DATA)}")
            print(f"  Escrever: {bool(mask & con.FILE_WRITE_DATA)}")
            print(f"  Executar: {bool(mask & con.FILE_EXECUTE)}")
            print(f"  Permissões especiais: {bool(mask & con.FILE_ALL_ACCESS)}")

def main():
    caminho_arquivo = r"C:\Program Files\Protheus_2210\smartclient.ini"
    verifica_permissao(caminho_arquivo)

if __name__ == "__main__":
    main()

