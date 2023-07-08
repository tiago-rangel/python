import ctypes
import win32security
import ntsecuritycon as con
import time
import sys

arquivo = "C:\\Program Files\\Protheus_2210\\smartclient.ini"

# Verificando se o programa está sendo executado por um usuário com privilégios de administrador
if ctypes.windll.shell32.IsUserAnAdmin():
    # Obtendo o SID dos usuários
    try:
        todos, domain, type = win32security.LookupAccountName("", "Todos")
    except:
        todos, domain, type = win32security.LookupAccountName("", "Everyone")
    try:
        usuarios, domain, type = win32security.LookupAccountName("", "Usuários")
    except:
        usuarios, domain, type = win32security.LookupAccountName("", "Users")

    # Obtendo as informações de segurança do arquivo
    sd = win32security.GetFileSecurity(arquivo, win32security.DACL_SECURITY_INFORMATION)

    # Obtendo a DACL atual do arquivo
    dacl = sd.GetSecurityDescriptorDacl()

    # Verificando se os usuários já possuem as permissões solicitadas
    todos_permissoes = False
    usuarios_permissoes = False
    
    for i in range(dacl.GetAceCount()):
        ace = dacl.GetAce(i)
        if ace[2] == todos:
            todos_permissoes = True
        elif ace[2] == usuarios:
            usuarios_permissoes = True
    
    if not (todos_permissoes and usuarios_permissoes):
        # Adicionando os usuários com permissão de modificar, ler e executar, leitura, gravação e permissões especiais
        dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_GENERIC_READ | con.FILE_GENERIC_WRITE | con.FILE_GENERIC_EXECUTE | con.DELETE | con.WRITE_DAC | con.WRITE_OWNER, todos)
        dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_GENERIC_READ | con.FILE_GENERIC_WRITE | con.FILE_GENERIC_EXECUTE | con.DELETE | con.WRITE_DAC | con.WRITE_OWNER, usuarios)

        # Atualizando as informações de segurança do arquivo
        sd.SetSecurityDescriptorDacl(1, dacl, 0)
        win32security.SetFileSecurity(arquivo, win32security.DACL_SECURITY_INFORMATION, sd)

        # Exibindo a mensagem na cor verde utilizando ANSI
        print("\033[32mPermissões do arquivo alteradas\033[0m")
        time.sleep(3)
else:
    # Verificando se o arquivo já foi previamente alterado
    sd = win32security.GetFileSecurity(arquivo, win32security.DACL_SECURITY_INFORMATION)
    dacl = sd.GetSecurityDescriptorDacl()
    
    try:
        todos, domain, type = win32security.LookupAccountName("", "Todos")
    except:
        todos, domain, type = win32security.LookupAccountName("", "Everyone")
    
    try:
        usuarios, domain, type = win32security.LookupAccountName("", "Usuários")
    except:
        usuarios, domain, type = win32security.LookupAccountName("", "Users")
    
    todos_permissoes = False
    usuarios_permissoes = False
    
    for i in range(dacl.GetAceCount()):
        ace = dacl.GetAce(i)
        if ace[2] == todos:
            todos_permissoes = True
        elif ace[2] == usuarios:
            usuarios_permissoes = True
    
    if not (todos_permissoes and usuarios_permissoes):
        # Exibindo a mensagem na cor vermelha utilizando ANSI
        print("\033[31mPara que o programa funcione favor executá-lo primeiro como administrador\033[0m")
        
        # Pausando a execução do programa por 3 segundos
        time.sleep(3)
        
        # Encerrando o programa
        sys.exit()
