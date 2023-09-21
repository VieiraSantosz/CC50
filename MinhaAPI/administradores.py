from flask import Flask, jsonify, request

app = Flask(__name__)

admins = [
    {
        'id'        : 1,
        'email'     : 'santos@gmail.com',
        'password'  : 'santos1234',
        'status'    : 'inativo',
        'type'      : 'vendedor',
        'date'      : '02/05/2002',
        'area'      : 'Real Madrid'
    }
]

### METÓDO POST PARA LOGIN DO USUÁRIO ###
@app.route('/admin/login', methods=['POST'])
def login_usuario():
    
    data = request.get_json()
    
    name = data.get('name')
    password = data.get('password')

    for admin in admins:
        if admin['name'] == name and admin['password'] == password:
            
            response = {
                'message': 'Login bem-sucedido',
                'id': admin['id'],
                'name': admin['name']
            }
            
            return jsonify(response), 200

    response = {'message': 'Credenciais inválidas'}
    return jsonify(response), 401
########################################  


app.run(port=5000, host='localhost', debug=True)