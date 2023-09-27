from flask import Flask, jsonify, request, session, mysql.connector

app = Flask(__name__)
app.secret_key = 'chave_secreta'

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='vieira1234',
    database='seboonline',
)

    
if conexao.is_connected():
    print("Conexão ao MySQL bem-sucedida!")

### METÓDO POST PARA CRIAR / REGISTRAR USUÁRIOS ###
    @app.route('/users/signup', methods=['POST'])
    def criar_usuario():
        
        novo_user = request.get_json()

        # Verifique se os campos necessários estão presentes no JSON
        if 'name' in novo_user and 'email' in novo_user and 'password' in novo_user and 'status' in novo_user and 'type' in novo_user:
            cursor = conexao.cursor()

            # Consulta SQL para inserir um novo usuário na tabela 'usuario'
            inserir_usuario_sql = "INSERT INTO usuarios (name, email, password, status, type) VALUES (%s, %s, %s, %s, %s)"

            # Execute a consulta SQL com os dados do novo usuário
            cursor.execute(inserir_usuario_sql, (novo_user['name'], novo_user['email'], novo_user['password'], novo_user['status'], novo_user['type']))

            # Faça commit das alterações no banco de dados
            conexao.commit()

            cursor.close()
            conexao.close()

            return jsonify({'message': 'Usuário criado com sucesso!'})
        else:
            return jsonify({'error': 'Campos obrigatórios ausentes no JSON'})
else:
    print("Não foi possível conectar com o MySql!!")
################################################### 


@app.route('/users/login', methods=['POST'])
def login_usuario():
    
    login = request.get_json()
    
    usuario = login.get('name')
    senha = login.get('password')
    
    cursor = conexao.cursor()

    # Consulta SQL para verificar as credenciais do usuário no banco de dados
    verificar_credenciais_sql = "SELECT id, name FROM usuario WHERE name = %s AND password = %s"
    
    cursor.execute(verificar_credenciais_sql, (usuario, senha))
    resultado = cursor.fetchone()

    cursor.close()

    if resultado:
        # As credenciais são válidas, crie uma sessão
        session['name'] = usuario

        response = {
            'id': resultado[0],
            'name': resultado[1],
            'message': 'Login Feito com Sucesso!'
        }
        return jsonify(response)
    else:
        response = {
            'message': 'Credenciais Inválidas!'
        }
        return jsonify(response)


app.run(port=5000, host='localhost', debug=True)