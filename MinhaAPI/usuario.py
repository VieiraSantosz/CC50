from flask import Flask, jsonify, request

app = Flask(__name__)


users = [
    {
        'id': 1,
        'Name': 'Vieira',
        'Password': 'vieira1234'
    },
    {
        'id': 2,
        'Name': 'Santos',
        'Password': 'santos1234'
    },
    {
        'id': 3,
        'Name': 'Rhayane',
        'Password': 'rhayane1234'
    },
]


### METÓDO GET PARA LISTAR USUÁRIOS ###
@app.route('/users', methods=['GET'])
def mostrar_usuario():
    return jsonify(users)
########################################


### METÓDO GET PARA LISTAR USUÁRIOS POR ID ###
@app.route('/users/<int:id>', methods=['GET'])
def mostrar_usuario_por_id(id):
    
    for user in users:
        if user.get('id') == id:
            return jsonify(user)
##############################################


### METÓDO PUT PARA EDITAR USUÁRIOS ###
@app.route('/users/<int:id>', methods=['PUT'])
def editar_usuario(id):
    editar_user = request.get_json()
    
    for i, novoUser in enumerate(users):
        if novoUser.get('id') == id:
            users[i].update(editar_user)
            return jsonify(users[i])
########################################


### METÓDO POST PARA LOGIN DO USUÁRIO ###
@app.route('/users/login', methods=['POST'])
def login_usuario():
    
    data = request.get_json()
    
    name = data.get('Name')
    password = data.get('Password')

    for user in users:
        if user['Name'] == name and user['Password'] == password:
            
            response = {
                'message': 'Login bem-sucedido',
                'id': user['id'],
                'Name': user['Name']
            }
            
            return jsonify(response), 200

    response = {'message': 'Credenciais inválidas'}
    return jsonify(response), 401
########################################  


### METÓDO POST PARA LOGOUT DO USUÁRIO ###
@app.route('/users/logout', methods=['POST'])
def logout_usuario():
    
    
    return "Usuário acabou de sair da sessão!"
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
    
    for i, delUser in enumerate(users):
        if delUser.get('id') == id:
            del users[i]
            
    return jsonify(users)
########################################     


app.run(port=5000, host='localhost', debug=True)