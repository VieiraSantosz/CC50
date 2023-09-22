from flask import Flask, jsonify, request, session

app = Flask(__name__)

admins = [
    {
        'id'        : 1,
        'name'      : 'Rhayane',
        'email'     : 'santos@gmail.com',
        'password'  : 'santos1234',
        'status'    : 'inativo',
        'type'      : 'vendedor',
        'date'      : '02/05/2002',
        'area'      : 'Real Madrid'
    }
]

users = [
    {
        'id'        : 1,
        'name'      : 'Vieira',
        'email'     : 'vieira@gmail.com',
        'password'  : 'vieira1234',
        'status'    : 'ativo',
        'type'      : 'comprador'
    },
    {
        'id'        : 2,
        'name'      : 'Santos',
        'email'     : 'santos@gmail.com',
        'password'  : 'santos1234',
        'status'    : 'inativo',
        'type'      : 'vendedor'
    },
    {
        'id'        : 3,
        'name'      : 'Rhayane',
        'email'     : 'rhayane@gmail.com',
        'password'  : 'rhayane1234',
        'status'    : 'ativo',
        'type'      : 'administrador'
    },
]


### METÓDO POST PARA LOGIN DE ADMIN ###
@app.route('/admin/login', methods=['POST'])
def login_admin():
    
    login = request.get_json()
    
    administrador   = login.get('name')
    senha           = login.get('password')

    for i in admins:
        if i['name'] == administrador and i['password'] == senha:
            
            session['name'] = administrador
            
            response = {
                'id'        : i['id'],
                'name'      : i['name'],
                'message'   : 'Login Feito com Sucesso!'
            }
            return jsonify(response)
        
        
        response = {
            'message': 'Credenciais Inválidas!'
        }
        return jsonify(response)
########################################  


### METÓDO POST PARA LOGOUT DE ADMIN ###
@app.route('/admin/logout', methods=['POST'])
def logout_admin():
    
    if 'name' in session:
        
        session.pop('name', None)
        response = {
            'message': 'Administrador acabou de sair da sessão!'
        }
        return jsonify(response)
    
    else:
        response = {
            'message': 'Nenhum Administrador logado!'
        }
        return jsonify(response)
########################################


### METÓDO GET PARA LISTAR USUÁRIOS ###
@app.route('/admin/users', methods=['GET'])
def mostrar_usuario():
    
    if 'name' not in session:
        response = {
            'message': 'Realize o Login primeiro!'
        }
        return jsonify(response)
    
    return jsonify(users)
########################################
 

app.secret_key = 'chave_secreta'
app.run(port=5000, host='localhost', debug=True)