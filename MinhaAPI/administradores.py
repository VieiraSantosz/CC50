from flask import Flask, jsonify, request

app = Flask(__name__)

admins = [
    {
        'id': 1,
        'Name': 'Real',
        'Password': 'Madrid'
    }
]

### METÓDO POST PARA LOGIN DO USUÁRIO ###
@app.route('/admin/login', methods=['POST'])
def login_usuario():
    
    data = request.get_json()
    
    name = data.get('Name')
    password = data.get('Password')

    for admin in admins:
        if admin['Name'] == name and admin['Password'] == password:
            
            response = {
                'message': 'Login bem-sucedido',
                'id': admin['id'],
                'Name': admin['Name']
            }
            
            return jsonify(response), 200

    response = {'message': 'Credenciais inválidas'}
    return jsonify(response), 401
########################################  


app.run(port=5000, host='localhost', debug=True)