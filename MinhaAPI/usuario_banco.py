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
################################################### 


### METÓDO PUT PARA EDITAR USUÁRIOS ###
    def editar_usuario(id):
        
        if 'name' not in session:
            response = {
                'message': 'Realize o Login primeiro!'
            }
            return jsonify(response)
        
        editar_user = request.get_json()
        
        cursor = conexao.cursor()

        # Consulta SQL para atualizar o usuário com base no ID
        atualizar_usuario_sql = "UPDATE usuario SET name = %s, email = %s, password = %s, status = %s, type = %s WHERE id = %s"
        
        cursor.execute(atualizar_usuario_sql, (editar_user['name'], editar_user['email'], editar_user['password'], editar_user['status'], editar_user['type'], id))

        # Faça commit das alterações no banco de dados
        conexao.commit()

        cursor.close()

        response = {
            'message': 'Usuário editado com sucesso!'
        }
        return jsonify(response)
########################################


### METÓDO DEL PARA DELETAR USUÁRIOS ###
    @app.route('/users/<int:id>', methods=['DELETE'])
    def excluir_usuario(id):
        if 'name' not in session:
            response = {
                'message': 'Realize o Login primeiro!'
            }
            return jsonify(response)
        
        cursor = conexao.cursor()

        # Consulta SQL para excluir o usuário com base no ID
        excluir_usuario_sql = "DELETE FROM usuario WHERE id = %s"
        
        cursor.execute(excluir_usuario_sql, (id,))

        # Faça commit das alterações no banco de dados
        conexao.commit()

        cursor.close()

        response = {
            'message': 'Usuário excluído com sucesso!'
        }
        return jsonify(response)
######################################## 


### METÓDO POST PARA LOGIN DO USUÁRIO ###
    @app.route('/users/login', methods=['POST'])
    def login_usuario():
        
        login = request.get_json()
        
        usuario = login.get('name')
        senha   = login.get('password')
        
        cursor = conexao.cursor()

        # Consulta SQL para verificar as credenciais do usuário no banco de dados
        verificar_credenciais_sql = "SELECT id, name FROM usuario WHERE name = %s AND password = %s"
        
        cursor.execute(verificar_credenciais_sql, (usuario, senha))
        resultado = cursor.fetchone()

        cursor.close()
        conexao.close()

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
########################################  


### METÓDO POST PARA LOGOUT DO USUÁRIO ###
    @app.route('/users/logout', methods=['POST'])
    def logout_usuario():
        if 'name' in session:
            # Remova a sessão do usuário
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

else:
    print("Não foi possível conectar com o MySql!!")

app.run(port=5000, host='localhost', debug=True)