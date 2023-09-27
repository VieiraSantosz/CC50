from flask import Flask, jsonify, request, session, mysql.connector

app = Flask(__name__)
app.secret_key = 'chave_secreta'

app.run(port=5000, host='localhost', debug=True)