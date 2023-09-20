import requests

user        =''
password    =''
headers     = {'Authorization': f'runas={user}'; f'key={password};'}

datype      = {'Content-type': 'application/json'}
proxy       = {'http': None,'https': None}


session = requests.session()
datype = {'Content-type': 'application/json'}
session.headers.update(headers)
session.proxies = proxy
session.trust_env = False
session.verify = False

baseUrl = "https://api.com"


def CadastroUser():

    userDados = {
        "Id"     : 1,
        "Nome"   : "Vieira",
        "Senha"  : "vieira1234",
        "Email"  : "vieira@gmail.com",
        "Status" : "ativo",
        "Tipo"   : "comprador"
    }
    
    cadastro = session.post(url = f'{baseUrl}/users/signup', headers=headers, json=userDados)
    
    if cadastro.status_code => 200 and <= 299:
        print("Usuário cadastrado com sucesso! | Código de status: ", cadastro.status_code)
        
    else if response.status_code => 400:
        print("Erro de validação. Verifique os dados do usuário. | Código de status: ", cadastro.status_code)
        
    else:
        print("Código de status:", cadastro.status_code)


def PostLogIn():
    login = session.post(url = f'{baseUrl}/users/login', verify=False) 
    
    infoLogin = json.loads(login.text)
    
    userId      = infoLogin['UserId']
    userName    = infoLogin['UserName']
    userEmail   = infoLogin['UserEmail']
    userSenha   = infoLogin['UserSenha']
    userStatus  = infoLogin['UserStatus']
    userTipo    = infoLogin['UserTipo']
    
    print("\nLogin Feito com Sucesso! - Código =", login.status_code)
    print("\nUserId:", userId, "\nUserName:", userName, "\nName:", name, 
          "\nEmail:", userEmail, "\nSenha:", userSenha, "\nStatus:", userStatus
          "\nTipo:", userTipo)
    print()
    
    
def PostLogOff():
    logoff = session.post(url = f'{baseUrl}/users/signout', verify=False) 

    print("\n\nUsuário acabou de sair da sessão! - Código =", logoff.status_code)
    print()