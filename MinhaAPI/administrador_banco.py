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
    
    
### METÓDO POST PARA LOGIN DE ADMINISTRADOR ###
    @app.route('/admin/login', methods=['POST'])
    def login_admin():
        
        login = request.get_json()
        
        administrador   = login.get('name')
        senha           = login.get('password')
        
        cursor = conexao.cursor()

        # Consulta SQL para verificar as credenciais do usuário no banco de dados
        verificar_credenciais_sql = "SELECT id, name FROM administrador WHERE name = %s AND password = %s"
        
        cursor.execute(verificar_credenciais_sql, (administrador, senha))
        resultado = cursor.fetchone()

        cursor.close()
        conexao.close()

        if resultado:
            # As credenciais são válidas, crie uma sessão
            session['name'] = administrador

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
    def logout_admin():
        
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


### METÓDO GET PARA LISTAR USUÁRIOS ###
    @app.route('/admin/users', methods=['GET'])
    def mostrar_usuario():
        
        if 'name' not in session:
            response = {
                'message': 'Realize o Login primeiro!'
            }
            return jsonify(response)
        
        cursor = conexao.cursor()

        # Consulta SQL para recuperar todos os usuários
        recuperar_usuarios_sql = "SELECT * FROM usuario"
        
        cursor.execute(recuperar_usuarios_sql)
        usuarios = cursor.fetchall()

        cursor.close()

        # Converter a lista de usuários em um formato JSON e retornar
        usuarios_json = [
            {
                'id'        : u[0], 
                'name'      : u[1], 
                'email'     : u[2], 
                'password'  : u[3], 
                'status'    : u[4], 
                'type'      : u[5]
            } 
        for u in usuario
        ]
        
        return jsonify(usuarios_json)
########################################


### METÓDO GET PARA LISTAR RELATÓRIOS E ESTATÍSTICAS ###
    @app.route('/admin/reports', methods=['GET'])
    def mostrar_relatorios_estatisticas():
        
        if 'name' not in session:
            response = {
                'message': 'Realize o Login primeiro!'
            }
            return jsonify(response)
        
        cursor = conexao.cursor()

        # Consulta SQL para recuperar relatórios e estatísticas
        recuperar_relatorios_sql = "SELECT * FROM relatorios"
        
        cursor.execute(recuperar_relatorios_sql)
        relatorios = cursor.fetchall()

        cursor.close()

        # Converter a lista de relatórios em um formato JSON e retornar
        relatorios_json = [
            {
                'id'        : r[0], 
                'titulo'    : r[1], 
                'conteudo'  : r[2]
            } 
            for r in relatorios
        ]
        
        return jsonify(relatorios_json)
########################################


else:
    print("Não foi possível conectar com o MySql!!")

app.run(port=5000, host='localhost', debug=True)