from flask import Flask, jsonify, request, session

app = Flask(__name__)


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


### METÓDO GET PARA LISTAR USUÁRIOS POR ID ###
@app.route('/users/<int:id>', methods=['GET'])
def mostrar_usuario_por_id(id):
    
    if 'name' not in session:
        response = {
            'message': 'Realize o Login primeiro!'
        }
        return jsonify(response)
    
    
    for user in users:
        if user.get('id') == id:
            return jsonify(user)
##############################################


### METÓDO PUT PARA EDITAR USUÁRIOS ###
@app.route('/users/<int:id>', methods=['PUT'])
def editar_usuario(id):
    
    if 'name' not in session:
        response = {
            'message': 'Realize o Login primeiro!'
        }
        return jsonify(response)
    
    editar_user = request.get_json()
    
    for i, novoUser in enumerate(users):
        if novoUser.get('id') == id:
            
            users[i].update(editar_user)
            return jsonify(users[i])
########################################


### METÓDO POST PARA LOGIN DO USUÁRIO ###
@app.route('/users/login', methods=['POST'])
def login_usuario():
    
    login = request.get_json()
    
    usuario     = login.get('name')
    senha       = login.get('password')

    for i in users:
        if i['name'] == usuario and i['password'] == senha:
            
            session['name'] = usuario
            
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


### METÓDO POST PARA LOGOUT DO USUÁRIO ###
@app.route('/users/logout', methods=['POST'])
def logout_usuario():
    
    if 'name' in session:
        
        session.pop('name', None)
        response = {
            'message': 'Usuário acabou de sair da sessão!'
        }
        return jsonify(response)
    
    else:
        response = {
            'message': 'Nenhum Usuário logado!'
        }
        return jsonify(response)
######################################## 


### METÓDO POST PARA CRIAR / REGISTRAR USUÁRIOS ###
@app.route('/users/signup', methods=['POST'])
def criar_usuario():
    
    novo_user = request.get_json()
    
    users.append(novo_user)
    return jsonify(users)
###################################################   


### METÓDO DEL PARA DELETAR USUÁRIOS ###
@app.route('/users/<int:id>', methods=['DELETE'])
def excluir_usuario(id):
    
    if 'name' not in session:
        response = {
            'message': 'Realize o Login primeiro!'
        }
        return jsonify(response)
    
    for i, delUser in enumerate(users):
        if delUser.get('id') == id:
            del users[i]
            
    return jsonify(users)
########################################     

app.secret_key = 'chave_secreta'
app.run(port=5000, host='localhost', debug=True)