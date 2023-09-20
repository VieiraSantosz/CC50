import requests

admin       =''
password    =''
headers     = {'Authorization': f'runas={admin}'; f'key={password};'}

datype      = {'Content-type': 'application/json'}
proxy       = {'http': None,'https': None}


session = requests.session()
datype = {'Content-type': 'application/json'}
session.headers.update(headers)
session.proxies = proxy
session.trust_env = False
session.verify = False

baseUrl = "https://api.com"


def PostLogIn():
    login = session.post(url = f'{baseUrl}/admin/login', verify=False) 
    
    infoLogin = json.loads(login.text)
    
    dataInicio  = infoLogin['data']
    areaEspec   = infoLogin['area']
    
    print("\nLogin Feito com Sucesso! - Código =", login.status_code)
    print("\nData de Início:", dataInicio, "n\,Área de Especialização:", areaEspec)
    print()