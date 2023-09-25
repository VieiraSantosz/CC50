1° pip install mysql-connector-python

2° Criar banco de dados no MySql
- CREATE DATABASE SeboOnline;
- USE SeboOnline;

3° Criar a tabela
- CREATE TABLE usuarios (
    idUser INT PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(10) NOT NULL,
    email VARCHAR(30) NOT NULL,
    password VARCHAR(30) NOT NULL,
    status VARCHAR(10) NOT NULL,
    type VARCHAR(20) NOT NULL
);

- CREATE TABLE administradores (
    idAdmin INT PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(10) NOT NULL,
    email VARCHAR(30) NOT NULL,
    password VARCHAR(30) NOT NULL,
    status VARCHAR(10) NOT NULL,
    type VARCHAR(20) NOT NULL,
    date DATE NOT NULL,
    area VARCHAR(20) NOT NULL
);

4° Código

import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='user',
    password='senha',
    database='banco de dados',
)

cursor = conexao.cursor()


# Adicionar info no banco de dados
nome    = "Vieira"
email   = "vieira@gmail.com"
senha   = "vieira1234"

comando = f'INSERT INTO nome_tabela (nome, email, senha) VALUES ("{nome}", "{email}", "{senha}")' 
cursos.execute(comando)

conexao.commit() #edita o seu banco de dados


# Ler info no banco de dados
comando = 'SELECT * FROM usuario' 
cursos.execute(comando)

conexao.commit() #edita o seu banco de dados
resultado = cursor.fetchall() #ler o banco de dados
print(resultado)


# Mudar info no banco de dados
nome    = "Vieira"
senha   = "santos1234"

comando = f'UPDATE usuario SET nome = "{nome}" WHERE senha = "{senha}"' 
cursos.execute(comando)

conexao.commit() #edita o seu banco de dados


# Deletar info no banco de dados
nome    = "Vieira"

comando = f'DELETE FROM usuario WHERE nome = "{nome}' 
cursos.execute(comando)

conexao.commit() #edita o seu banco de dados

cursos.close()
conexao.close()